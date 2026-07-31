print("📚 KNOWLEDGE BRAIN LOADED")

knowledge = {
    "your name": "I'm ChatMate, powered by KABAI AI 🤖",
    "creator": "I was created by Tshepo Kabai.",
    "what is python": "Python is a programming language used to create software, websites, AI, and automation tools.",
    "what is ai": "AI means Artificial Intelligence — computer systems that can perform tasks that usually require human intelligence."
}

def answer(question):

    question = question.lower()

    return knowledge.get(
        question,
        "I don't know that yet, but I'm still learning."
    )