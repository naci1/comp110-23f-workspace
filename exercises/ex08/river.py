"""File to define River class."""

__author__ = "730652828"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """The check_ages method removes a fish if the fish age is greater than 3 and if the bear age is greater than 5."""
        new_bear_list: list[Bear] = []
        new_fish_list: list[Fish] = []
        # iterating through the original list of Bears
        bear_idx: int = 0
        fish_idx: int = 0
        while bear_idx < len(self.bears):
            if self.bears[bear_idx].age <= 3:
                new_bear_list.append(self.bears[bear_idx])
            bear_idx += 1
        self.bears = new_bear_list
        while fish_idx < len(self.fish):
            if self.fish[fish_idx].age <= 5:
                new_fish_list.append(self.fish[fish_idx])
            fish_idx += 1
        self.fish = new_fish_list
        return None

    def bears_eating(self):
        """If there are at least 5 fish in the river, the bear will eat 3 fish."""
        idx: int = 0
        while idx < len(self.bears):
            if len(self.fish) > 5:
                self.remove_fish(3)
                self.bears[idx].eat(3)
            idx += 1


        return None
    
    def check_hunger(self):
        """If the hunger_score of bear < 0, we remove Bear from the river."""
        idx: int = 0
        while idx < len(self.bears):
            if self.bears[idx].hunger_score < 0:
                self.bears.pop(idx)
            idx += 1
        return None
        
    def repopulate_fish(self):
        """Every pair of fish will produce 2 more fish."""
        idx: float = 0.0
        size_of_fish_list: int = len(self.fish)
        while idx < size_of_fish_list:
            new_fish: Fish = Fish()
            self.fish.append(new_fish)
            idx += 0.5

        return None
    
    def repopulate_bears(self):
        """A pair of bears will produce 1 bear."""
        idx: int = 0
        size_of_bear_list: int = len(self.bears)
        while idx < size_of_bear_list:
            new_bear: Bear = Bear()
            self.bears.append(new_bear)
            idx += 2
        return None
    
    def view_river(self):
        """This prints the amount of fish and bears for a specific day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        
    
    def one_river_week(self):
        idx: int = 0
        # calls the function one_river_day() 7 times
        while idx < 7:
            self.one_river_day()
            idx += 1
    
    def remove_fish(self, amount: int):
        counter: int = 0
        while counter< amount:
            self.fish.pop(0)
            counter += 1

            
