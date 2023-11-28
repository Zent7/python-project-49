import random

MIN_START = 1
MAX_START = 10
MIN_DIFF = 1
MAX_DIFF = 5
MIN_LENGTH = 5
MAX_LENGTH = 10
NUM_QUESTIONS_TO_WIN = 3


def main():
    brain_progression()


def generate_progression(length):
    start = random.randint(MIN_START, MAX_START)
    diff = random.randint(MIN_DIFF, MAX_DIFF)
    progression = [start + i * diff for i in range(length)]
    return progression


def hide_number(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_number = progression[hidden_index]
    progression[hidden_index] = ".."
    return hidden_number, progression


def brain_progression():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(NUM_QUESTIONS_TO_WIN):
        progression_length = random.randint(MIN_LENGTH, MAX_LENGTH)
        progression = generate_progression(progression_length)
        hidden_number, progression_with_hidden = hide_number(progression)

        print("What number is missing in the progression?")
        print("Question:", " ".join(map(str, progression_with_hidden)))

        user_answer = int(input("Your answer: "))

        if user_answer == hidden_number:
            print("Correct!")
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
