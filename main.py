import language_brain

print("🤖 KABAI AI: Hello! Type 'bye' to end the chat.")

while True:
    message = input("You: ")

    if message.lower() == "bye":
        print("🤖 KABAI AI: Goodbye! 👋")
        break

    response = language_brain.respond(message)
    print("🤖 KABAI AI:", response)