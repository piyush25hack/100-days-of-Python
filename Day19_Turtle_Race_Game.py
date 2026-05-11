from turtle import Turtle, Screen
import random
all_turtles = []
race_on = False

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title ="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x =-230, y=y_position[turtle_index])
    all_turtles.append(tim)
    
if user_bet:
    race_on = True
    
while race_on:
    for tim in all_turtles:
        if tim.xcor()>180:
            race_on = False
            winning_color = tim.pencolor()
            if winning_color == user_bet:
                print(f"You have Won!  The {winning_color} turtle is the winner")
            else:
                print(f"You have Lost!  The {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        tim.forward(random_distance)

screen.exitonclick()