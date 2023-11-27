import random

MIN_NUMBER = 1
MAX_NUMBER = 100
NUM_ANSWERS_TO_WIN = 3


def main():
    brain_even()


def even(number):
    return number % 2 == 0


def brain_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')

    score = 0
    while score < NUM_ANSWERS_TO_WIN:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        print('Answer "yes" if the number is even, '
              'otherwise answer "no".')
        print(f'Question: {number}')
        user_answer = input('Your answer: ').lower()

        if (user_answer == 'yes' and even(number)) or \
           (user_answer == 'no' and not even(number)):
            print('Correct!')
            score += 1
        else:
            correct_answer = 'yes' if even(number) else 'no'
            print(
                f"'{user_answer}' is the wrong answer; "
                f"the correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
