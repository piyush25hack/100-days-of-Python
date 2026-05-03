# import colorgram

# colors = colorgram.extract(
#     "/Users/piyushnamdev/Desktop/100_Days_of_Python/Day18_Colorgram_Project/image.png",
#     6
# )

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

# Original Progrma from here after extracting the value

from turtle import Turtle , Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129)]

dots = 100
tim.setheading(250)
tim.forward(300)
tim.setheading(0)
for dot_count in range(1 ,dots+1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    
    if dot_count %10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
screen.exitonclick()