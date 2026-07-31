print("🧠 LANGUAGE BRAIN LOADED")

def respond(message):

    message = message.lower()

    if "hello" in message:
        return "Hey there! 👋"

    elif "how are you" in message:
        return "I'm doing great! 😄"

    elif "your name" in message:
        return "I'm KABAI AI 🤖"

    else:
        return "I'm still learning. Teach me more!"