"""TODO: This scence just contains a stereotypical subarb with greenary, trees, a house, a river, and a flower. It is also a sunny day and the sun is present!"""
 
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
    epic_flower: Turtle = Turtle()
    epic_river: Turtle = Turtle()

    rectangle(ground, -300, -250, 600, 150, "green", "green")
    house(epic_house, -200, -100)
    tree(epic_tree_1, 100, -100, 1)
    tree(epic_tree_2, 200, -100, 0.5)
    Circle(sun, -250, 165, 50, "yellow", "yellow", 360)
    Flower(epic_flower, 10, -100, 30, 60, 15)
    River(epic_river, -42, -250, 50, 173, "blue")
    done()


def rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float, fcolor: str, pcolor: str) -> None:
    """This function creates a rectangle that can be used multiple times throughout the program. 
    
    It takes a length and width parameter and I can change the fill color and pen color.
    """
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
    """This function provides the code for a triangle that can be used in our code. 
    
    It makes a triangle with different fill colors and pencolors.
    """
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
    """This function provides the code for the triangular roof and square base.

    It makes use of the Door procedure that I built.
    """
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    # broke down the house component into 3 simpler procedures "Door, roof(triangle), and base of the house(rectangle) (lines 87-89) to satisfy "Above and beyond" category(7)
    rectangle(a_turtle, x, y, 190, 190, "yellow", "orange")
    triangle(a_turtle, x, y + 190, 190, "orange", "blue")
    Door(a_turtle, x + (95 / 2), y, 95, 95)


def tree(a_turtle: Turtle, x: float, y: float, shrink_factor: float) -> None:
    """This function provides the code for a tree. The tree can not be taller than the house. Therefore, I introduced a shrink_factor to make the other trees smaller.

    I also used the xcor() and ycor() command (to satisfy the "Above and beyond" category(8), lines 104-105) to be used to find the position of x after creating a rectangle.
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
    """This method makes use of the built in circle command (to satisfy the "Above and beyond" category(8), line 125) to be used multiple times throughout the program.

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
    """This method makes a door to our house using the rectangle and Circle commands. 
    
    It also creates a doorknob using the Circle command created.
    """
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    rectangle(a_turtle, x, y, door_length, door_width, "gray", "black")
    Circle(a_turtle, x + 80, y + 50, 5, "blue", "blue", 360)


def Flower(a_turtle: Turtle, x: float, y: float, f_length: float, f_width: float, petal_radius: float) -> None:
    """This method creates a tiny flower that grows near the house. 

    It consists of the Circle and Rectangle commands to help aid in making the flower.
    """
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    rectangle(a_turtle, x, y, f_length, f_width, "brown", "brown")
    new_pos_x: float = a_turtle.xcor()
    new_pos_y: float = a_turtle.ycor()
    a_turtle.forward(f_length)
    a_turtle.left(90)
    a_turtle.forward(f_width)
    Circle(a_turtle, new_pos_x + f_length, new_pos_y + f_width, f_length * (1 / 2), "pink", "red", 360)


def River(a_turtle: Turtle, x: float, y: float, r_length: float, r_width: float, fcolor: str) -> None: 
    """This method creates a river that flows through the ground near the house.

    I used only a fill color as the river is blue and changed the degrees to 60 and 120.
    """
    a_turtle.speed(SPEED)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.fillcolor(fcolor)
    i: int = 0
    while i < 2:
        a_turtle.forward(r_length)
        a_turtle.left(60)
        a_turtle.forward(r_width)
        a_turtle.left(120)
        i += 1
    a_turtle.end_fill()


if __name__ == "__main__":
    main()