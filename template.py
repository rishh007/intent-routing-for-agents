"""
Minimal Agentic Intent Router
----------------------------

A clean template for routing user queries into workflows
using intent classification + entity extraction.

LLM-agnostic | Domain-agnostic | Agent-ready
"""

import json
from typing import TypedDict, Dict

# Define the state 

class AgentState(TypedDict, total=False):
    user_query: str
    intent: str
    entities: Dict
    result: str


# 2. LLM Wrapper (Mock / Replace)

def call_llm(prompt: str) -> str:
    """
    Replace this with OpenAI / Ollama / Claude / Gemini
    Must return a STRING.
    """
    print("\n--- LLM PROMPT ---")
    print(prompt)
    print("------------------\n")

    # Mock response for demo
    return '{"intent": "analyze"}'


# 3. Intent Classification

ALLOWED_INTENTS = [
    "retrieve",
    "analyze",
    "visualize",
    "generate",
    "help"
]

def classify_intent(state: AgentState) -> AgentState:
    prompt = f"""
You are an intent router.

Allowed intents:
{ALLOWED_INTENTS}

User query:
"{state['user_query']}"

Return ONLY JSON:
{{ "intent": "<intent>" }}
"""

    response = call_llm(prompt)

    try:
        intent = json.loads(response)["intent"]
        if intent not in ALLOWED_INTENTS:
            intent = "help"
    except Exception:
        intent = "help"

    state["intent"] = intent
    return state


# 4. Entity Extraction

def extract_entities(state: AgentState) -> AgentState:
    prompt = f"""
Extract structured parameters from the query.
Return ONLY JSON.

Possible fields:
- target
- timeframe
- format

Query:
"{state['user_query']}"
"""

    response = call_llm(prompt)

    try:
        state["entities"] = json.loads(response)
    except Exception:
        state["entities"] = {}

    return state


# 5. Define / import workflows

def retrieve_workflow(state: AgentState) -> AgentState:
    state["result"] = f"📦 Retrieving data for {state['entities']}"
    return state

def analyze_workflow(state: AgentState) -> AgentState:
    state["result"] = f"📊 Analyzing data for {state['entities']}"
    return state

def visualize_workflow(state: AgentState) -> AgentState:
    state["result"] = f"📈 Visualizing data for {state['entities']}"
    return state

def generate_workflow(state: AgentState) -> AgentState:
    state["result"] = f"📝 Generating output for {state['entities']}"
    return state

def help_workflow(state: AgentState) -> AgentState:
    state["result"] = "🤖 I can retrieve, analyze, visualize or generate."
    return state


# 6. Intent Router

WORKFLOW_MAP = {
    "retrieve": retrieve_workflow,
    "analyze": analyze_workflow,
    "visualize": visualize_workflow,
    "generate": generate_workflow,
    "help": help_workflow
}

def route(state: AgentState) -> AgentState:
    workflow = WORKFLOW_MAP.get(state["intent"], help_workflow)
    return workflow(state)


def run_agent(query: str):
    state: AgentState = {"user_query": query}

    state = extract_entities(state)
    state = classify_intent(state)
    state = route(state)

    return state["result"]


if __name__ == "__main__":
    print("\n🔥 Agentic AI Template 🔥\n")

    while True:
        query = input("You > ")
        if query.lower() in {"exit", "quit"}:
            break

        output = run_agent(query)
        print(f"Agent > {output}\n")
