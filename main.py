# import colorgram
#
# rgb_colors=[]
# colors=colorgram.extract('images.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)

dot=Turtle()


color_list=[(16, 35, 48), (59, 94, 113), (201, 135, 158), (128, 77, 103), (237, 162, 184), (174, 101, 131), (246, 191, 202), (62, 26, 52), (22, 79, 95), (139, 152, 173), (107, 39, 70), (52, 62, 80), (115, 120, 154), (250, 214, 212), (196, 205, 216), (92, 139, 155), (115, 94, 94), (187, 187, 205), (73, 82, 81), (149, 118, 118), (167, 181, 181), (46, 71, 70), (166, 145, 144), (42, 65, 64), (199, 185, 185), (179, 197, 197), (201, 217, 216), (183, 194, 200)]

dot.speed(0)
dot.penup()
dot.hideturtle()
dot.setheading(225)
dot.forward(300)
dot.setheading(0)
number_of_dots=1000
for dot_count in range(1,number_of_dots+1):
    dot.dot(20,random.choice(color_list))
    dot.forward(50)
    if dot_count%10==0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)










screen=Screen()
screen.exitonclick()