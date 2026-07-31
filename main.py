import language_brain
import calculator
import memory

print("🤖 KABAI AI: Hello! Type 'bye' to end the chat.")

while True:
    message = input("You: ")

    if message.lower() == "bye":
        print("🤖 KABAI AI: Goodbye! 👋")
        break

    if message.lower().startswith("remember"):
        data = message.replace("remember", "").strip()

        if "=" in data:
            key, value = data.split("=", 1)
            print("🤖 KABAI AI:", memory.remember(key.strip(), value.strip()))
        else:
            print("🤖 KABAI AI: Use format: remember name=Tshepo")

    elif message.lower().startswith("what is"):
        key = message.replace("what is", "").strip()
        print("🤖 KABAI AI:", memory.recall(key))

    elif any(symbol in message for symbol in ["+", "-", "*", "/"]):
        print("🤖 KABAI AI:", calculator.calculate(message))

    else:
        print("🤖 KABAI AI:", language_brain.respond(message))