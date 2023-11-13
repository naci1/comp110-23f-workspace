"""File to define Bear class."""

class Bear:

    age: int
    hunger_score: int
    
    def __init__(self):
        """Initializing the bear constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """This is a method that incremenets and decrements hunger everyday by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """This is a method that increments the hunger_score by the number of fish eaten by the bear."""
        self.hunger_score += num_fish
