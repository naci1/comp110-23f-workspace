"""Summing the elements of a list using different loops"""

__author__ = "730652828"

"""This calculates the sum of a list of floats using a while loop"""
def w_sum(vals: list[float]) -> float:
    counter: int = 0; # this allows us to iterate through the loop
    sum: float = 0.0 # initializes the sum of the list to 0
    while counter < len(vals):
        sum += vals[counter]
        counter += 1
    return sum


"""This calculates the sum of a list of floats using a for loop without range"""
def f_sum(vals: list[float]) -> float:
    sum: float = 0 #initializes the sum of the list to 0
    for value in vals:
        sum += value
    return sum

"""This calculates the sum of a list of floats using a for loop with the "range" function"""
def f_range_sum(vals: list[float]) -> float:
    sum: float = 0 #initializes the sum of the list to 0
    for idx in range(len(list)):
        sum += vals[idx]
    return sum
    
    