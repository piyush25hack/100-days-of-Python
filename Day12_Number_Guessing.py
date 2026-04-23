from random import randint

Easy_level_Turns = 10
Hard_level_Turns = 5

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return Easy_level_Turns 
    else:
        return Hard_level_Turns

def guess(user_guess, actual, Turns):
    if user_guess > actual:
        print("Too High")
        return Turns - 1
    elif user_guess < actual:
        print("Too Low")
        return Turns - 1
    else:
        print(f"You got the answer! The answer was {actual}")
        return 0

print("Welcome to the Number Guessing Game!")

def game():
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    Turns = difficulty()
    
    user = 0
    while user != answer and Turns > 0:
        print(f"\nYou have {Turns} attempts remaining to guess the number.")
        user = int(input("Make a guess: "))
        Turns = guess(user, answer, Turns)
        
        if Turns > 0 and user != answer:
            print("Guess again!")
    
    if user != answer:
        print(f"\nGame over! The number was {answer}.")

game()