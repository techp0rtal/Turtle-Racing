import random
from turtle import Turtle, Screen, clearscreen, reset

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# tim.penup()
# tim.goto(x=-230, y=0)
starting_y_locations = [-60, -30, 0, 30, 60, 90]
turtles_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_y_locations[turtle_index])
    turtles_list.append(new_turtle)

#I don't get how this works when we're reusing the same object 6 times

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in turtles_list:
        if racer.xcor() >230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            print(racer.color())
        random_distance = random.randint(0, 10)
        racer.forward(random_distance)




def move_forward():
    new_turtle.forward(10)


def move_backward():
    new_turtle.backward(10)


def turn_right():
    new_turtle.right(10)

def turn_left():
    new_turtle.left(10)

def reset_screen():
    clearscreen()
    reset()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=reset_screen)
screen.exitonclick()












#etch a sketch
# from turtle import Turtle, Screen, clearscreen, reset
#
# tim = Turtle()
# screen = Screen()
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_right():
#     tim.right(10)
#
# def turn_left():
#     tim.left(10)
#
# def reset_screen():
#     clearscreen()
#     reset()
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="s", fun=move_backward)
# screen.onkeypress(key="d", fun=turn_right)
# screen.onkeypress(key="a", fun=turn_left)
# screen.onkeypress(key="c", fun=reset_screen)
# screen.exitonclick()