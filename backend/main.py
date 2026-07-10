from fastapi import FastAPI
from agents.pilot import pilot_agent
from agents.builder import builder_agent
from agents.debugger import debugger_agent
from memory.vector_store import store_memory, retrieve_memory

app = FastAPI()

@app.get("/")
def home():
    return {"AMRHZ": "AI SYSTEM ONLINE 🚀"}

@app.get("/chat")
def chat(prompt: str):
    memory = retrieve_memory(prompt)

    plan = pilot_agent(prompt, memory)
    result = builder_agent(plan)
    debug = debugger_agent(result)

    store_memory(prompt, debug)

    return {
        "response": debug
    }
