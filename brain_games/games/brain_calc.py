import random

MIN_NUMBER = 1
MAX_NUMBER = 100
NUM_QUESTIONS_TO_WIN = 3


def main():
    brain_calc()


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def calculate_answer(num1, num2, operation):
    if operation == '+':
        return plus(num1, num2)
    elif operation == '-':
        return minus(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)


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

        if user_answer.isdigit():
            if str(user_answer) == str(correct_answer):
                print('Correct!')
                score += 1
            else:
                print(
                    f"'{user_answer}' is the wrong answer; "
                    f"the correct answer was '{correct_answer}'."
                )
                print(f"Let's try again, {name}!")
                return
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
