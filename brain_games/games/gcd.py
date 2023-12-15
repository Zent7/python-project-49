import random
import math

MIN_NUMBER = 1
MAX_NUMBER = 100
NUM_QUESTIONS_TO_WIN = 3


def main():
    brain_gcd()


def brain_gcd():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    score = 0
    while score < NUM_QUESTIONS_TO_WIN:
        num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        correct_gcd = math.gcd(num1, num2)

        print(f"Question: {num1} {num2}")

        user_gcd = int(input("Your answer: "))

        if user_gcd == correct_gcd:
            score += 1
            print("Correct!")
        else:
            print(f"'{user_gcd}' is the wrong answer ;(. "
                  f"Correct answer was '{correct_gcd}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
