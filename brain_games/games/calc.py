import random

MIN_NUMBER = 1
MAX_NUMBER = 100
NUM_QUESTIONS_TO_WIN = 3

def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def generate_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])
    expression = f'{num1} {operation} {num2}'
    correct_answer = calculate_answer(num1, num2, operation)
    return expression, correct_answer

def calculate_answer(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2

def game_logic():
    return generate_question()

def display_question(question):
    print(f"Question: {question}")

def get_user_answer():
    return input("Your answer: ")

def display_result(is_correct, correct_answer=None):
    if is_correct:
        print("Correct!\n")
    else:
        print(f"Sorry, your answer is wrong. Correct answer was '{correct_answer}'.\n")
        print("Let's try again, {name}!\n")
        raise SystemExit

def main():
    name = welcome_user()
    instruction = "What is the result of the expression?"
    play_game(game_logic, instruction, display_question, get_user_answer, display_result)

if __name__ == "__main__":
    main()