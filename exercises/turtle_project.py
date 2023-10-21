"""TODO: This scence just contains a stereotypical subarb with greenary, a house and some trees. It is also a sunny day!"""
 
__author__ = "730652828"
 
from turtle import Turtle, colormode, done 
colormode(255)

# this is the global variable for the speed of all the Turtle commands
SPEED = 100


def main() -> None:
    """The entrypoint of my scene."""
    ground: Turtle = Turtle()
    epic_house: Turtle = Turtle()
    epic_tree_1: Turtle = Turtle()
    epic_tree_2: Turtle = Turtle()
    sun: Turtle = Turtle()
    rectangle(ground, -300, -250, 600, 150, "green", "green")
    house(epic_house, -200, -100)
    tree(epic_tree_1, 100, -100, 1)
    tree(epic_tree_2, 200, -100, 0.5)
    Circle(sun, -250, 165, 50, "yellow", "yellow", 360)
    done()


def rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float, fcolor: str, pcolor: str) -> None:
    """This function creates a rectangle that can be used multiple times throughout the program."""
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.fillcolor(fcolor)
    a_turtle.pencolor(pcolor)
    i: int = 0
    while i < 2:
        a_turtle.forward(length)
        a_turtle.left(90)
        a_turtle.forward(width)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()


def triangle(a_turtle: Turtle, x: float, y: float, length: float, fcolor: str, pcolor: str) -> None:
    """This function provides the code for a triangle that can be used in our code."""
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.pencolor(pcolor)
    a_turtle.fillcolor(fcolor)
    i: int = 0
    while i < 3:
        a_turtle.forward(length)
        a_turtle.left(120) 
        i += 1
    a_turtle.end_fill()


def house(a_turtle: Turtle, x: float, y: float) -> None:
    """This function provides the code for the triangular roof and square base."""
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    rectangle(a_turtle, x, y, 190, 190, "yellow", "orange")
    triangle(a_turtle, x, y + 190, 190, "orange", "blue")
    Door(a_turtle, x + (95 / 2), y, 95, 95)


def tree(a_turtle: Turtle, x: float, y: float, shrink_factor: float) -> None:
    """This function provides the code for a tree. The tree can not be taller than the house. Therefore, we introduced a shrink_factor to make the other trees smaller.

    I also used the xcor() and ycor() command (to satisfy the "Above and beyond" category) to be used to find the position of x after creating a rectangle.
    """
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    rectangle(a_turtle, x, y, 50 * shrink_factor, 200 * shrink_factor, "brown", "brown")
    rectangle(a_turtle, x - (50 * shrink_factor), y + (200 * shrink_factor), 150 * shrink_factor, 50 * shrink_factor, "green", "green")
    new_pos_x: float = a_turtle.xcor()
    new_pos_y: float = a_turtle.ycor()
    a_turtle.forward(150 * shrink_factor)
    a_turtle.left(90)
    a_turtle.forward(50 * shrink_factor)
    Circle(a_turtle, new_pos_x + 150 * shrink_factor, new_pos_y + 50 * shrink_factor, (150 * shrink_factor) / 2, "green", "green", 180)


def Circle(a_turtle: Turtle, x: float, y: float, radius: float, fcolor: str, pcolor: str, angle: float) -> None:
    """This method makes use of the built in circle command (to satisfy the "Above and beyond" category) to be used multiple times throughout the program.

    It uses the fill color and pencolor to change the border and fill color of the circles.
    """
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.fillcolor(fcolor)
    a_turtle.pencolor(pcolor)
    a_turtle.circle(radius, angle)
    a_turtle.end_fill()


def Door(a_turtle: Turtle, x: float, y: float, door_length: float, door_width: float) -> None:
    """This method makes a door to our house. It also creates a doorknob using the Circle command created."""
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    rectangle(a_turtle, x, y, door_length, door_width, "gray", "black")
    Circle(a_turtle, x + 80, y + 50, 5, "blue", "blue", 360)


if __name__ == "__main__":
    main()