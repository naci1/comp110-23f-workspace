"""File to define Fish class."""

__author__ = "730652828"


class Fish:
    """Creates a Fish class."""

    age: int
    
    def __init__(self):
        """Initializing the fish constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """This method adds 1 to the age of a given fish."""
        self.age += 1
        return None