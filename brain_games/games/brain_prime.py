import random

MIN_NUMBER = 1
MAX_NUMBER = 100
NUM_WINS_TO_END = 3


def main():
    brain_prime()


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def display_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print('Answer "yes" if the given number is prime. Otherwise answer "no".')
    print(f"Question: {number}")
    return number


def get_user_answer():
    return input("Your answer: ").lower()


def display_result(is_correct):
    if is_correct:
        print("Correct!\n")
    else:
        print("Sorry, your answer is wrong. The correct answer is 'yes' if the given number is prime. Otherwise answer 'no'.\n")
        raise SystemExit 


def brain_prime():
    name = welcome_user()
    wins = 0

    try:
        while wins < NUM_WINS_TO_END:
            number = display_question()
            user_answer = get_user_answer()

            correct_answer = 'yes' if is_prime(number) else 'no'
            is_correct = (user_answer == correct_answer)

            display_result(is_correct)

            if is_correct:
                wins += 1

        print(f"Congratulations, {name}!")

    except KeyboardInterrupt:
        print("\nGoodbye!")
        raise SystemExit


if __name__ == "__main__":
    main()