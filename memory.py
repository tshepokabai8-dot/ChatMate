import json

print("💾 MEMORY BRAIN LOADED")

FILE = "memory.json"

try:
    with open(FILE, "r") as f:
        memories = json.load(f)
except:
    memories = {}


def remember(user, key, value):
    if user not in memories:
        memories[user] = {}

    memories[user][key] = value

    with open(FILE, "w") as f:
        json.dump(memories, f)

    return "I'll remember that."


def recall(user, key):
    if user in memories:
        return memories[user].get(key, "I don't remember that yet.")

    return "I don't remember that yet."