"""This class allows us to work with Point objects."""



from __future__ import annotations


class Point: 
    """This class contains an x and y attribute."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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


    


       
