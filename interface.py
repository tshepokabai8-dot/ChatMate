import tkinter as tk

import language_brain
import calculator
import memory
import personality
import knowledge
import security
import settings
import voice


def start():

    def send_message():
        message = user_input.get()
        user_input.delete(0, tk.END)

        chat_box.insert(tk.END, "You: " + message + "\n")

        if not security.check_message(message):
            response = "I can't help with that request."

        elif any(symbol in message for symbol in ["+", "-", "*", "/"]):
            response = calculator.calculate(message)

        else:
            response = knowledge.answer(message)

            if response == "I don't know that yet, but I'm still learning.":
                response = language_brain.respond(message)

        final_response = personality.style(str(response))

        chat_box.insert(tk.END, final_response + "\n\n")

        voice.speak(final_response)


    window = tk.Tk()
    window.title(
        f"{settings.APP_NAME} — Powered by {settings.POWERED_BY}"
    )
    window.geometry("450x600")

    chat_box = tk.Text(window, height=25, width=50)
    chat_box.pack()

    user_input = tk.Entry(window, width=40)
    user_input.pack()

    send_button = tk.Button(
        window,
        text="Send",
        command=send_message
    )
    send_button.pack()

    window.mainloop()