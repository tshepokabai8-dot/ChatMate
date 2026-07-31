import language_brain
import calculator

print("🤖 KABAI AI: Hello! Type 'bye' to end the chat.")

while True:
    message = input("You: ")

    if message.lower() == "bye":
        print("🤖 KABAI AI: Goodbye! 👋")
        break

    if any(symbol in message for symbol in ["+", "-", "*", "/"]):
        result = calculator.calculate(message)
        print("🤖 KABAI AI:", result)

    else:
        response = language_brain.respond(message)
        print("🤖 KABAI AI:", response)