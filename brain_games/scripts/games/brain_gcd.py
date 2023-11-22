import random
import math

def main():
    brain_gcd()

def brain_gcd():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    score = 0
    while score < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_gcd = math.gcd(num1, num2)
        
        print(f"Question: {num1} {num2}")
        
        user_gcd = int(input("Your answer: "))
        
        if user_gcd == correct_gcd:
            score += 1
            print("Correct!")
        else:
            print(f"'{user_gcd}' is the wrong answer ;(. Correct answer was '{correct_gcd}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()