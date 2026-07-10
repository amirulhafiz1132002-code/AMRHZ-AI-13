from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.pilot import pilot_agent
from agents.builder import builder_agent
from agents.debugger import debugger_agent

from memory.vector_store import store_memory, retrieve_memory

app = FastAPI()

# CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "AMRHZ AI ONLINE 🚀"}

@app.get("/chat")
def chat(prompt: str):
    memory = retrieve_memory(prompt)

    plan = pilot_agent(prompt, memory)
    result = builder_agent(plan)
    checked = debugger_agent(result)

    store_memory(prompt, checked)

    return {"response": checked}
