"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730652828"


class Simpy:
    """Simpy class for various numerical purposes!"""
    
    values: list[float]

    def __init__(self, given_list: list[float]):
        """Constructor. Assigns a list of float values to the attribute "values" which is a list of floats."""
        self.values = given_list
    
    def __str__(self) -> str:
        """It lets us know that we are trying to learn about simpy. Magic method."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, iterations: int) -> None:
        """Fills the attribute "values" with a value specific number of times."""
        for i in range(iterations):
            self.values.append(value)
    
    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fills the attribute "values" with a range of values starting from a starting value to a stop value."""
        value_to_append: float = start
        assert step != 0.0
        while(value_to_append != stop):
            self.values.append(start)
            start += step
            value_to_append = start
    
    def sum(self) -> float:
        """Returns the sum of all the values in the attribute "values" list."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overloaded the plus operator to add a simpy object + float or simpy object + simpy object."""
        new_list: list[float] = []
        if type(rhs) is float:
            for i in range(len(self.values)):
                new_list.append(self.values[i] + rhs)
            new_simpy_object: Simpy = Simpy(new_list)
        
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                new_list.append(self.values[i] + rhs.values[i])
            new_simpy_object: Simpy = Simpy(new_list)
        
        return new_simpy_object
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overloaded the power operator to calculate something to the power of another thing for simpy object ** simpy object or simpy object ** float."""
        new_list: list[float] = []
        if type(rhs) is float:
            for i in range(len(self.values)):
                new_list.append(self.values[i] ** rhs)
            new_simpy_object: Simpy = Simpy(new_list)
        
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                new_list.append(self.values[i] ** rhs.values[i])
            new_simpy_object: Simpy = Simpy(new_list)

        return new_simpy_object

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overloaded the "==" to test whether the elements in the attribute list are the same as another float values or another Simpy list."""
        bool_list: list[bool] = []
        if type(rhs) is float:
            for i in range(len(self.values)):
                if(self.values[i] == rhs):
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                if(self.values[i] == rhs.values[i]):
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        return bool_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overloaded the ">" to test whether the elements in the attribute list are greater than another float values or another Simpy list."""
        bool_list: list[bool] = []
        if type(rhs) is float:
            for i in range(len(self.values)):
                if(self.values[i] > rhs):
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                if(self.values[i] > rhs.values[i]):
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        return bool_list
    
    def __getitem__(self, rhs: int) -> float:
        """Returns the value at a particular index for the values attribute."""
        return self.values[rhs]
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns the value of """
        if type(rhs) is int:
            return self.values[rhs]
        else:
            assert len(rhs) == len(self.values)
            new_list: list[float] = []
            for i in range(len(self.values)):
                if rhs[i] == True:
                    new_list.append(self.values[i])
            new_simpy_object: Simpy = Simpy(new_list)
            return new_simpy_object