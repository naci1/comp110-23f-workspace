"""TODO: Describe your scene program."""
 
__author__ = "730652828"
 
from turtle import Turtle, colormode, done 
colormode(255)
 
 
def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    ground: Turtle = Turtle()
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    rectangle(ground, -300, -100, 600, 150)
    done()


# TODO: Define the procedures for other components in your scene here.
def rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    """This function creates a rectangle that can be used multiple times throughout the program."""
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.color("green")
    i: int = 0
    while i < 2:
        a_turtle.forward(length)
        a_turtle.right(90)
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()

def triangle(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """This function provides the code for a triangle that can be used in our code."""
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.pencolor(0,0,255)
    a_turtle.fillcolor("orange")
    
def house(a_turtle: Turtle, x: float, y: float) -> None:
    """This function provides the code for the triangular roof and square base."""
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.pencolor(255, 0, 0)
    a_turtle.fillcolor(128, 128, 128)
    rectangle(a_turtle, x, y, 400, 400)


    


#def window():
    

#def door():


#def tree():
    

#def sun():


  




# TODO: Use the __name__ is "__main__" idiom shown in class

if __name__ == "__main__":
    main()