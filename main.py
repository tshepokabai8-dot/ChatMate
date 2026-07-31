import language_brain
import calculator
import memory
import personality
import knowledge

print("🤖 ChatMate — Powered by KABAI AI")
print("Type 'bye' to exit.")

while True:
    message = input("You: ")

    if message.lower() == "bye":
        print(personality.style("Goodbye! 👋"))
        break

    if message.lower().startswith("remember"):
        data = message.replace("remember", "").strip()

        if "=" in data:
            key, value = data.split("=", 1)
            response = memory.remember(key.strip(), value.strip())
        else:
            response = "Use format: remember name=Tshepo"

    elif message.lower().startswith("what is"):
        key = message.replace("what is", "").strip()
        response = memory.recall(key)

    elif any(symbol in message for symbol in ["+", "-", "*", "/"]):
        response = str(calculator.calculate(message))

    else:
        response = knowledge.answer(message)

        if response == "I don't know that yet, but I'm still learning.":
            response = language_brain.respond(message)

    print(personality.style(response))