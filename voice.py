import pyttsx3

print("🎤 VOICE SYSTEM LOADED")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()