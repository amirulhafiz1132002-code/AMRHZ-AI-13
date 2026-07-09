import csv

BRAIN_FILE = "brain_v2.csv"

def save_new_memory(intent, response):
    with open(BRAIN_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["new", intent, "auto", "low", response])