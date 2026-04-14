import random

stages = ['''+---+
  |   |
      |
      |
      |
      |
=========''',  
'''+---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''+---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

word_list = ["apple", "tiger", "plane"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

lives = 6
game_over = False
guessed_letters = []   # ✅ bahar define

# print(chosen_word)  

while not game_over:
    guess = input("Guess a letter: ").lower()

    # ✅ repeat check
    if guess in guessed_letters:
        print("Already guessed")
        continue
    else:
        guessed_letters.append(guess)

    # ✅ check correct/wrong
    if guess in chosen_word:
        print("Correct!")
    else:
        print("Wrong!")
        lives -= 1

    # ✅ update display
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # ✅ clean display
    print(" ".join(display))
    print(stages[6 - lives])

    # ✅ win condition
    if "_" not in display:
        print("You win!")
        game_over = True

    # ✅ lose condition
    if lives == 0:
        print("You lose!")
        print("Word was:", chosen_word)
        game_over = True