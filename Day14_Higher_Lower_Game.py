print("""
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")

import random
score = 0
game_continue = True

    
data = [
    {"name": "Instagram", "followers": 600},
    {"name": "Cristiano Ronaldo", "followers": 620},
    {"name": "Ariana Grande", "followers": 380},
    {"name": "Dwayne Johnson", "followers": 400},
    {"name": "Kylie Jenner", "followers": 410},
    {"name": "Selena Gomez", "followers": 430},
    {"name": "Virat Kohli", "followers": 260},  
    {"name": "Narendra Modi", "followers": 90},
    {"name": "Taylor Swift", "followers": 300},  
    {"name": "Elon Musk", "followers": 200}
]
# Variable defined here for comparison 

account_b = random.choice(data)

#created function for account 
def format_data(account):
    account_name = account["name"]
    account_follower = account["followers"]
    return f"{account_name} has {account_follower} million followers"

#created function for check_answer from user
def check_answer(user_guess, a_follower, b_follower):
    """Take a user's guess and the followers count"""
    if a_follower > b_follower:
         return user_guess =="a"
    else:
        return user_guess =="b"
# Made while loop condition just for looping the game 
while game_continue:
        # Generate random accounts
        account_a = account_b
        account_b = random.choice(data)

        # Ensure different accounts
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print("VS")
        print(f"Against B: {format_data(account_b)}")

        #who has more followers

        guess = input("Who has more followers ? Type 'A' or Type 'B': ").lower()
        
        #print clear statement here
        print("\n"*20)

        #Get Follower count 
        a_follower_count = account_a ["followers"]
        b_follower_count = account_b["followers"]

        check = check_answer(guess,a_follower_count, b_follower_count)

        #Give user feedback on their guess.

        if check :
            score +=1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong answer. Final score: {score}")
            game_continue = False