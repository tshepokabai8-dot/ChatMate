print("🔒 SECURITY SYSTEM LOADED")

blocked_words = [
    "hack",
    "virus",
    "malware"
]

def check_message(message):

    message = message.lower()

    for word in blocked_words:
        if word in message:
            return False

    return True