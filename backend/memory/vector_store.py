memory_db = []

def store_memory(prompt, response):
    memory_db.append((prompt, response))

def retrieve_memory(query):
    for p, r in memory_db:
        if query in p:
            return r
    return ""