"""TODO: Describe your scene program."""
 
__author__ = "730652828"
 
from turtle import Turtle, colormode, done 
colormode(255)
 
 
def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    ground: Turtle = Turtle()
    epic_house: Turtle = Turtle()
    epic_tree: Turtle = Turtle()
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    rectangle(ground, -300, -250, 600, 150, "green", "green")
    house(epic_house,-200 ,-100)
    tree(epic_tree, 0, -100)
    done()


# TODO: Define the procedures for other components in your scene here.
def rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float, fcolor:str, pcolor:str) -> None:
    """This function creates a rectangle that can be used multiple times throughout the program."""
    a_turtle.penup()
    a_turtle.goto(x,y)
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

def triangle(a_turtle: Turtle, x: float, y: float, length: float, fcolor: str, pcolor:str) -> None:
    """This function provides the code for a triangle that can be used in our code."""
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.pencolor(pcolor)
    a_turtle.fillcolor(fcolor)
    i: int = 0
    while i < 3:
        a_turtle.forward(length)
        a_turtle.left(120) 
        i = i+1
    a_turtle.end_fill()


def house(a_turtle: Turtle, x: float, y: float) -> None:
    """This function provides the code for the triangular roof and square base."""
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.pendown()
    rectangle(a_turtle, x, y, 190, 190, "yellow", "orange")
    triangle(a_turtle, x, y + 190, 190, "orange", "blue")


def tree(a_turtle: Turtle, x: float, y: float):
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.pendown()
    rectangle(a_turtle, x, y, 50, 200, "brown", "brown")
    rectangle(a_turtle, x-50, y, 150 , 50, "green", "green")
    

# TODO: Use the __name__ is "__main__" idiom shown in class

if __name__ == "__main__":
    main()