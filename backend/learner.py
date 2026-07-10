import json

def auto_learn(prompt, response):
    try:
        with open("../data/memory.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({"prompt": prompt, "response": response})

    with open("../data/memory.json", "w") as f:
        json.dump(data, f, indent=2)