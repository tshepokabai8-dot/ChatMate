import json

print("👤 PROFILE SYSTEM LOADED")

FILE = "profiles.json"

try:
    with open(FILE, "r") as f:
        profiles = json.load(f)
except:
    profiles = {}

def create_profile(name):
    profiles[name] = {
        "name": name
    }

    with open(FILE, "w") as f:
        json.dump(profiles, f)

    return "Profile created for " + name

def get_profile(name):
    return profiles.get(name, "Profile not found.")