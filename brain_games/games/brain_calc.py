import random

MIN_NUMBER = 1
MAX_NUMBER = 100
NUM_QUESTIONS_TO_WIN = 3


def main():
    brain_calc()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def calculate_answer(num1, num2, operation):
    result = 0
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    
    return int(result)  


def generate_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])
    expression = f'{num1} {operation} {num2}'
    correct_answer = str(calculate_answer(num1, num2, operation))
    return expression, correct_answer


def brain_calc():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')

    score = 0
    while score < NUM_QUESTIONS_TO_WIN:
        expression, correct_answer = generate_question()

        print('What is the result of the expression?')
        print(f'Question: {expression}')
        user_answer = input('Your answer: ')

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_answer == correct_answer or user_answer == int(correct_answer):
            print('Correct!')
            score += 1
        else:
            print(
                f"'{user_answer}' is the wrong answer; "
                f"the correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()