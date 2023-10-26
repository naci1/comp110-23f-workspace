"""EX06 - Dictionary Functions."""

__author__ = "730652828"

def invert(given_dict: dict[str, str]) -> dict[str,str]:
    keys_of_dict: list[str] = []
    values_of_dict: list[str] = []
    for key in given_dict:
        keys_of_dict.append(key)
        values_of_dict.append(given_dict[key])
    
    # define an inverted list
    inverted_dict: dict[str, str] = {}

    # iterate through one of the lists
    for i in range(len(given_dict)):
        inverted_dict[values_of_dict[i]] = keys_of_dict[i]    
    # check whether the keys in the inverted_dict are duplicated or not
    for value in given_dict:
        if value in given_dict == value in inverted_dict:
            raise KeyError("duplicate keys are present in the inverted dictionary.")
  
    return inverted_dict


def favorite_colors(given_dict: dict[str,str]) -> str:
    counter: int = 0
    while counter < len(given_dict):
        
        
    

    
    