print("🤖 KABAI AI: Hello! Type 'bye' to end the chat.")

while True:
    message = input("You: ")

    if message.lower() == "hello":
        print("🤖 KABAI AI: Hey there! 👋")

    elif message.lower() == "how are you?":
        print("🤖 KABAI AI: I'm doing great! Thanks for asking 😄")

    elif message.lower() == "bye":
        print("🤖 KABAI AI: Goodbye! 👋")
        break

    else:
        print("🤖 KABAI AI: I don't understand that yet, but I'm learning!")