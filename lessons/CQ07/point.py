"""This class allows us to work with Point objects."""
from __future__ import annotations


class Point: 
    """This class contains an x and y attribute."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Assigns the x and y values to the attributes."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """This allows us to scale the x and y values in the attributes."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """This creates a new Point object and scales the x and y values and returns that new point object."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """This returns a readable string in the form of x: [number]; y:[number]."""
        point_string: str = f"x: {self.x}; y: {self.y}"
        return point_string

    def __mul__(self, factor: int | float) -> Point:
        """This multiplies the x and y values by a factor value."""
        self.x *= factor
        self.y *= factor
        newpoint: Point = Point(self.x, self.y)
        return newpoint
    
    def __add__(self, number_to_add: int | float):
        """This adds a number to the x and y values in the point by the same value."""
        self.x += number_to_add
        self.y += number_to_add
        newpoint: Point = Point(self.x, self.y)
        return newpoint

    
    


    


       
