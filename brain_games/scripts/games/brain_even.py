import random

def main():
    brain_even()

def even(number):
    return number % 2 == 0 

def brain_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')

    score = 0
    while score < 3:
        number = random.randint(1, 100)
        print(f'Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question:{number}')
        user_answer = input('Your answer: ').lower()

        if (user_answer == 'yes' and even(number)) or (user_answer == 'no' and not even(number)):
            print('Correct!')
            score += 1
        else:
            if even(number):
                correct_answer = 'yes'
            else:
                correct_answer = 'no'

            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return 
    print(f'Congratulations, {name}!')    
          
if __name__ == "__main__":
    main()