import tkinter as tk
import language_brain
import calculator

print("🖥️ CHAT INTERFACE LOADED")

def send_message():
    message = user_input.get()
    user_input.delete(0, tk.END)

    chat_box.insert(tk.END, "You: " + message + "\n")

    if any(symbol in message for symbol in ["+", "-", "*", "/"]):
        response = calculator.calculate(message)
    else:
        response = language_brain.respond(message)

    chat_box.insert(tk.END, "ChatMate: " + str(response) + "\n\n")


window = tk.Tk()
window.title("ChatMate — Powered by KABAI AI")
window.geometry("400x500")

chat_box = tk.Text(window)
chat_box.pack()

user_input = tk.Entry(window)
user_input.pack()

send_button = tk.Button(
    window,
    text="Send",
    command=send_message
)
send_button.pack()

window.mainloop()