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


def brain_prime():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    wins = 0

    while wins < NUM_WINS_TO_END:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        print('Answer "yes" if given number is prime. '
              'Otherwise answer "no".')
        print(f"Question: {number}")

        user_answer = input("Your answer: ").lower()

        if (user_answer == 'yes' and is_prime(number)) or \
           (user_answer == 'no' and not is_prime(number)):
            print("Correct!")
            wins += 1
        else:
            correct_answer = 'yes' if is_prime(number) else 'no'
            print(f"Sorry, '{user_answer}' is wrong. "
                  f"The correct answer is {correct_answer}.")
            return

    print(f"Congratulations, {name}! You've won {NUM_WINS_TO_END} times.")


if __name__ == "__main__":
    main()
