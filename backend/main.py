from fastapi import FastAPI
from rag import retrieve_memory, save_memory
from agents import run_agents
from voice import process_voice
from learner import auto_learn

app = FastAPI()

@app.get("/")
def root():
    return {"AMRHZ": "AI SYSTEM ONLINE 🚀"}

@app.post("/chat")
def chat(prompt: str):
    context = retrieve_memory(prompt)
    result = run_agents(prompt, context)
    save_memory(prompt, result)
    auto_learn(prompt, result)
    return {"response": result}

@app.post("/voice")
def voice(input: str):
    return {"response": process_voice(input)}