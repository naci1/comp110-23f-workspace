"""Defining a Class!"""


from __future__ import annotations


"""
Think of a class defintion as a "roadmap" for objects that belong to the class.
You are defining the underlying structure that 
every instance of that class will have.
"""

class Pizza:
    """This is my class to represent pizza."""

    #attributes
    #syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    # self passes pizza object as a parameter
    def __init__(self, size: str, toppings: int, gf: bool):

        #self.size is changing the attribute values

        """Constructor"""

        # updating the attributes with values in the argument
        self.size = size
        self.toppings = toppings
        self.gluten_free = gf



        # returns "self"
    
    # self is the pizza object, so you do not pass the "object reference"
    def price(self) -> float:
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75(self.toppings)
        if self.gluten_free:
            cost += 100
        return cost
    
    def add_toppings(self, num_toppings: int):
        """Updates existing pizza order with num_toppings."""
        self.toppings += num_toppings

    def add_toppings_new_order(self, num_toppings: int) -> Pizza:
        """Make a new pizza order using existing info"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza



    

    

    