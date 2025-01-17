"""EX04 - 'list' Utility functions!"""

__author__ = "730652828"


def all(int_list: list[int], int_to_be_searched: int) -> bool:
    """This function takes an integer list of integers and tries to see if all the integers in that list are equal to a target integer."""
    counter: int = 0

    # if the length of the list is 0, then automatically return false as there is nothing to check
    if len(int_list) == 0:
        return False

    # a counter is initialized to traverse through the list
    while counter < len(int_list):
        
        # try to check whether the element in that particular index of the list is NOT equal to the value to be searched
        if int_list[counter] != int_to_be_searched:
            
            # return false and exit out of the loop
            return False
        
        # increment the counter and goes to the next value in the list
        counter += 1

    # all elements are equal to the integer to be searched and we return True.
    return True


def max(int_list: list[int]) -> int:
    """This function takes an integer list and returns the max value."""
    # this raises a value error due to the fact that there are no elements in the integer list.
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        
        # initalizes max to the first value of the list
        max: int = int_list[0]

        # initializes a counter variable to traverse through the array.
        counter: int = 1
        while counter < len(int_list):
            if int_list[counter] > max:
                
                # assign the max value to the element inside that particular index of int_list
                max = int_list[counter]

            # increment the counter and goes to the next value in the list
            counter += 1

        # returns the max value
        return max
  

def is_equal(int_list_one: list[int], int_list_two: list[int]) -> bool:
    """This function tries to check if every element at every index of two lists are the same."""
    # if the sizes of the two lists are not the same then the function automatically returns False and exits out of the function
    if len(int_list_one) != len(int_list_two):
        return False
    
    # initalizes a counter to traverse through the entire array
    counter: int = 0

    # since the size of both lists are the same we can write the while loop to check for one of the lists 
    while counter < len(int_list_one):
        
        # checks if the element of every index of both lists are the same
        if int_list_one[counter] != int_list_two[counter]:
            
            # returns False if the elements are not the same
            return False
        counter += 1
    
    # returns True because all the elements at every index are exactly the same
    return True
        
          
    

  
            
        

          
        
    
