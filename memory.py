print("💾 MEMORY BRAIN LOADED")

memory = {}

def remember(key, value):
    memory[key] = value
    return "I'll remember that."

def recall(key):
    return memory.get(key, "I don't remember that yet.")