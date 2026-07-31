import language_brain
import calculator
import memory
import personality
import knowledge
import settings
import security
import profile
import updates

current_user = "default"

print(f"🤖 {settings.APP_NAME} — Powered by {settings.POWERED_BY}")
print(f"Version: {settings.VERSION}")
print("Type 'bye' to exit.")

while True:
    message = input("You: ")

    if not security.check_message(message):
        print(personality.style("I can't help with that request."))
        continue

    if message.lower() == "bye":
        print(personality.style("Goodbye! 👋"))
        break

    if message.lower() == "check updates":
        response = updates.check_update()

    elif message.lower().startswith("login"):
        current_user = message.replace("login", "").strip()
        response = "Welcome back, " + current_user

    elif message.lower().startswith("remember"):
        data = message.replace("remember", "").strip()

        if "=" in data:
            key, value = data.split("=", 1)
            response = memory.remember(
                current_user,
                key.strip(),
                value.strip()
            )
        else:
            response = "Use format: remember favorite=anime"

    elif message.lower().startswith("what is"):
        key = message.replace("what is", "").strip()
        response = memory.recall(current_user, key)

    elif any(symbol in message for symbol in ["+", "-", "*", "/"]):
        response = calculator.calculate(message)

    else:
        response = knowledge.answer(message)

        if response == "I don't know that yet, but I'm still learning.":
            response = language_brain.respond(message)

    print(personality.style(str(response)))