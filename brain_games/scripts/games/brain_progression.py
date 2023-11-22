import random

def main():
    brain_progression()

def generate_progression(length):
    start = random.randint(1, 10)
    diff = random.randint(1, 5)
    progression = [start + i * diff for i in range(length)]
    return progression

def hide_number(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_number = progression[hidden_index]
    progression[hidden_index] = ".."
    return hidden_number, progression

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3): 
        progression_length = random.randint(5, 10)
        progression = generate_progression(progression_length)
        hidden_number, progression_with_hidden = hide_number(progression)

        print("What number is missing in the progression?")
        print("Question:", " ".join(map(str, progression_with_hidden)))

        user_answer = int(input("Your answer: "))

        if user_answer == hidden_number:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            print("Let's try again,", name)
            break
    else:
        print("Congratulations,", name, "You've completed the game!")

if __name__ == "__main__":
    main()