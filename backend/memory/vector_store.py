import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def store_memory(prompt, response):
    data = load_memory()
    data.append({"prompt": prompt, "response": response})
    save_memory(data)

def retrieve_memory(query):
    data = load_memory()
    for item in data:
        if query.lower() in item["prompt"].lower():
            return item["response"]
    return ""
