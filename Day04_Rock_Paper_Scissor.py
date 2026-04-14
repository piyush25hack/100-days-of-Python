import random
rock ='''
      _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
 '''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
 '''
gamelist = [rock, paper, scissor]
usr = int(input("What do you choose ? Type 0 for Rock, Type 1 for paper, Type 2 for scissor\n"))
if usr>=0 and usr <=2:
 print(gamelist[usr])
computer_choice = random.randint(0,2)
print(f"Computer Chose:")
print(gamelist[computer_choice])
if usr >= 3 or usr < 0:
     print("You type an invalid number")
elif usr == 0 and computer_choice ==2:
  print("You Win")
elif computer_choice ==0 and usr==2:
     print("You lose!")
elif computer_choice > usr:
     print("You Lose!")
elif usr >computer_choice:
     print("You win!")
elif computer_choice ==0 and usr==0:
     print("It's a draw ")
