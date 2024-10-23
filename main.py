import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red","orange","yellow","green","blue","purple"]
y_position = -70
all_turtles = []


for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position)
    y_position += 30
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You win! {winning_color} won the race.")

            else:
                print(f"You lose! {winning_color} won the race.")

        new_distance = random.randint(0, 10)
        turtle.forward(new_distance)


screen.exitonclick()