import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # prompt ke liye title set karna
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                              prompt="What's another state name?").title()
    
    if answer == "Exit":
        # List comprehension ka use karke missing states dhundna
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") # 'to.csv' nahi 'to_csv' hota hai
        break
        
    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # FILTERING KO FIX KIYA:
        state_data = data[data.state == answer]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer)