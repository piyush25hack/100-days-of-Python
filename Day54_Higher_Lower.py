from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)
print(f"Debug: Random number is {random_number}")  # Console mein dikhega

@app.route('/')
def home():
    return '''
    <h1>Guess a number between 0 and 9</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="400">
    '''

@app.route('/<int:guess>')
def check_guess(guess):
    if guess < random_number:
        return '''
        <h1 style="color: blue;">{} is too low!</h1>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="400">
        '''.format(guess)
    elif guess > random_number:
        return '''
        <h1 style="color: red;">{} is too high!</h1>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="400">
        '''.format(guess)
    else:
        return '''
        <h1 style="color: green;">{} is correct! 🎉</h1>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="400">
        '''.format(guess)

if __name__ == '__main__':
    app.run(debug=True)