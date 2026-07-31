print("🧮 CALCULATOR BRAIN LOADED")

def calculate(problem):
    try:
        answer = eval(problem)
        return answer
    except:
        return "I couldn't solve that."