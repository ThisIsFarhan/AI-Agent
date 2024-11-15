from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import re


llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key = "",
    temperature=0,
)

class Agent:
    def __init__(self, system=""):
        self.messages = []
        if system:
            self.messages.append(SystemMessage(content=system))
    
    def __call__(self, message):
        self.messages.append(HumanMessage(content=message))
        result = self.execute()
        self.messages.append(AIMessage(content=result))
        return result

    def execute(self):
        response = llm.invoke(self.messages)
        return response.content

def calculate(what):
    return eval(what)

def planet_mass(name):
    masses = {
        "Mercury": 0.33011,
        "Venus": 4.8675,
        "Earth": 5.972,
        "Mars": 0.64171,
        "Jupiter": 1898.19,
        "Saturn": 568.34,
        "Uranus": 86.813,
        "Neptune": 102.413,
    }
    return f"{name} has a mass of {masses[name]} x 10^24 kg"

def query(prompt):
    action_re = re.compile(r"^Action: (\w+): (.*)$")
    max_turns = int(input("Enter the maximum number of turns: "))
    i = 0
    bot = Agent(prompt)
    
    while i < max_turns:
        i += 1
        question = input("You: ")
        result = bot(question)
        print("Bot:",result)
        actions = [action_re.match(a) for a in result.split("\n") if action_re.match(a)]
        if actions:
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception("Unkown action: {}: {}".format(action, action_input))
            print("Running {} {}".format(action, action_input))
            observation = known_actions[action](action_input)
            print("Observation:", observation)
            next_prompt = "Observation: {}".format(observation)
            result = bot(next_prompt)
            print("Bot:", result)
        else:
            return


known_actions = {"calculate": calculate, "planet_mass": planet_mass}

if __name__ == "__main__":
    prompt = """
        You run in a loop of Thought, Action, PAUSE, Observation.
        At the end of the loop you output an Answer.
        Use Thought to describe your thoughts about the question you have been asked, use thought only the first time.
        Use Action to run one of the actions available to you - then return PAUSE.
        Observation will be the result of running those actions.

        Your available actions are:

        calculate:
        e.g. calculate: 4 * 7 / 3
        Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

        planet_mass:
        e.g. planet_mass: Earth
        return the mass of a planet in the solar system

        Example session:

        Question: What is the combined mass of Earth and Mars?
        Thought: I should find the mass of each planet using planet_mass.
        Action: planet_mass: Earth
        PAUSE

        You will be called again with this:

        Observation: Earth has a mass of 5.972 x 10^24 kg

        You then output:
        
        Answer: Earth has a mass of 5.972 x 10^24 kg

        Next, call the agent again with the following without using thought:

        Action: planet_mass: Mars
        PAUSE

        Observation: Mars has a mass of 0.64171 x 10^24 kg

        You then output:

        Answer: Mars has a mass of 0.64171 x 10^24 kg

        Finally, calculate the combined mass.

        Action: calculate: 5.971 + 0.64171 (dont use exponent here)
        PAUSE

        Observation: The combined mass is 6.61371 x 10^24 kg

        Answer: The combined mass of Earth and Mars is 6.61371 x 10^24 kg    
    """.strip()

    agent = Agent(system=prompt)
    # response = agent("What is the mass of Earth?")
    # print(response)

    # response = planet_mass("Earth")
    # print(response)

    # next_response = f"Observation: {response}"
    # print(next_response)

    # response = agent(next_response)
    # print(response)

    # print(f"Messages -> {agent.messages}")

    # -------Complex--------
    # question = "what is the combined mass of Earth and Mars?"
    # response = agent(question)
    # print(response)

    # next_prompt = "Observation: {}".format(planet_mass("Earth"))
    # print(next_prompt)

    # response = agent(next_prompt)
    # print(response)

    # next_prompt = "Observation: {}".format(planet_mass("Mars"))
    # print(next_prompt)

    # res = agent(next_prompt)
    # print(res)

    # next_prompt = "Observation: {}".format(eval("5.972 + 0.64171"))
    # print(next_prompt)

    # res = agent(next_prompt)
    # print(res)

    #-------------Automating-----------------
    query(prompt)


