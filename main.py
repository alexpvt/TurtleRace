import turtle as t
import random

race_on = False
win = t.Screen()
win.setup(width=500, height=400)
user_bet = win.textinput(title="Make your bet", prompt="Wich turtle should win ? Enter color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_position[turtle])
    all_turtle.append(new_turtle)


if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You WIN !!! {winning_color} turtle wan race")
            else:
                print(f"You LOST :( {winning_color} turtle wan race")

        speed = random.randint(0, 7)
        turtle.forward(speed)



win.exitonclick()