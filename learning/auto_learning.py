import csv

BRAIN_FILE = "data/brain_v2.csv"

def load_brain():
    data = []
    try:
        with open(BRAIN_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("[ERROR] Brain file not found.")
    return data


def score_memory(row, intent):
    score = 0
    if row.get("intent") == intent:
        score += 3
    if row.get("priority") == "high":
        score += 2
    if row.get("context_tag") == "auto":
        score += 1
    return score


def find_best_match(intent):
    brain = load_brain()
    best = None
    best_score = -1

    for row in brain:
        score = score_memory(row, intent)
        if score > best_score:
            best_score = score
            best = row

    return best