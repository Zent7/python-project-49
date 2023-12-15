NUM_QUESTIONS_TO_WIN = 3

def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def display_question(question):
    print(f"Question: {question}")

def get_user_answer():
    return input("Your answer: ")

def display_result(is_correct, correct_answer=None):
    if is_correct:
        print("Correct!\n")
    else:
        print(f"'{correct_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print("Let's try again!\n")
        raise SystemExit

def play_game(game_logic, instruction):
    name = welcome_user()
    score = 0

    while score < NUM_QUESTIONS_TO_WIN:
        print(instruction)
        question, correct_answer = game_logic()
        display_question(question)
        user_answer = get_user_answer()

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        is_correct = (user_answer == correct_answer)
        display_result(is_correct, correct_answer)

        if is_correct:
            score += 1

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    def game_logic():
        raise NotImplementedError("You should implement the game_logic function in your specific game file.")

    instruction = "This is a generic game. Replace this instruction in your specific game file."
    play_game(game_logic, instruction)  