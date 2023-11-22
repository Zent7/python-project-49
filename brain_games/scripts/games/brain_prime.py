import random

def main():
    brain_prime()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    while True:
        number = random.randint(1, 100)
        print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
        print(f"Question: {number}")

        user_answer = input("Your answer: ").lower()

        if user_answer == 'yes' and is_prime(number):
            print("Correct!")
        elif user_answer == 'no' and not is_prime(number):
            print("Correct!")
        else:
            correct_answer = 'yes' if is_prime(number) else 'no'
            print(f"Sorry, '{user_answer}' is wrong. The correct answer is {correct_answer}.")
        return

if __name__ == "__main__":
    main()