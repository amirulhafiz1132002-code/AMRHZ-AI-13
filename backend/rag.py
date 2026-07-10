from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
memory = []

def save_memory(prompt, response):
    text = prompt + " " + response
    emb = model.encode([text])
    index.add(np.array(emb))
    memory.append(text)

def retrieve_memory(query):
    if len(memory) == 0:
        return ""
    emb = model.encode([query])
    D, I = index.search(np.array(emb), 3)
    return "\n".join([memory[i] for i in I[0] if i < len(memory)])