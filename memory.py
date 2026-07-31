import json

print("💾 MEMORY BRAIN LOADED")

FILE = "memory.json"

try:
    with open(FILE, "r") as f:
        memory = json.load(f)
except:
    memory = {}

def remember(key, value):
    memory[key] = value

    with open(FILE, "w") as f:
        json.dump(memory, f)

    return "I'll remember that."

def recall(key):
    return memory.get(key, "I don't remember that yet.")