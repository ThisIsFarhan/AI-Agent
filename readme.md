# AI Agent from Scratch

## Overview

This repository contains the implementation of a custom AI Agent built from scratch using Python. The agent is designed to simulate reasoning, action execution, and response generation based on user queries. It incorporates **LangChain** components and a **Large Language Model (LLM)** (`llama-3.1-70b-versatile`) to handle natural language understanding and perform dynamic computations or data retrieval.

## Features

- **Custom AI Agent**:  
  Implements a loop of reasoning, action execution, and observation before generating a final answer.

- **Dynamic Actions**:  
  The agent supports predefined actions such as:
  - **Mathematical calculations** (e.g., `4 * 7 / 3`)
  - **Planet mass retrieval** for planets in the solar system.

- **LLM Integration**:  
  Powered by **LangChain** and **Groq API**, enabling natural language understanding and response generation.

## Workflow

The agent follows a structured workflow:
1. **Thought**:  
   The agent considers the steps required to answer the question.
   
2. **Action**:  
   Executes a predefined action based on the query.

3. **Observation**:  
   The result of the action is returned as an observation.

4. **Answer**:  
   The agent uses the observation to generate a final response.

### Example Workflow

**Question**: What is the combined mass of Earth and Mars?  
1. **Thought**: I should find the mass of each planet using the `planet_mass` action.  
2. **Action**: Retrieve the mass of Earth.  
   **Observation**: Earth has a mass of 5.972 x 10^24 kg.  
3. **Action**: Retrieve the mass of Mars.  
   **Observation**: Mars has a mass of 0.64171 x 10^24 kg.  
4. **Action**: Perform the calculation `5.972 + 0.64171`.  
   **Observation**: The combined mass is 6.61371 x 10^24 kg.  
5. **Answer**: The combined mass of Earth and Mars is 6.61371 x 10^24 kg.

## Tech Stack

- **Python**: Core language for development.
- **LangChain**: Framework for building applications with LLMs.
- **Groq API**: For invoking the `llama-3.1-70b-versatile` LLM.
- **Regular Expressions (Regex)**: For parsing and processing agent responses.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   conda create --name venv python=3.10.15
   git clone https://github.com/ThisIsFarhan/AI-Agent.git
   cd ai-agent-from-scratch
