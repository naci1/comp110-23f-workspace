"""EX06 - Dictionary Functions."""

__author__ = "730652828"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """This function takes a given_dict and inverts the values of the list by switching the key and value pairs and returns the new inverted dict. If two values in the original list are the same a Key_error will be produced."""
    inverted_dict: dict[str, str] = {}
    temp_value = ""
    for key in given_dict:
        temp_value = given_dict[key]
        if temp_value in inverted_dict:
            raise KeyError("Multiple keys are present in the inverted list!")
        else:
            inverted_dict[temp_value] = key
    return inverted_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """This function takes a given_dict and returns a string for the value that appears most in the list. If two values appear the most the same amount of times, the function returns the value that appeared first in the list."""
    temp_color: str = ""
    temp_counter: int = 0
    max_color_counter: int = 0
    max_color_appearance: str = ""
    for key in given_dict:
        temp_color = given_dict[key]
        temp_counter = 0
        for key in given_dict:
            if given_dict[key] == temp_color:
                temp_counter += 1
        if temp_counter > max_color_counter:
            max_color_counter = temp_counter
            max_color_appearance = temp_color
    return max_color_appearance


def count(given_list: list[str]) -> dict[str, int]:
    """This function produces a dictionary which contains a key and the value of the key is the number of times that key appears in the list."""
    empty_dict: dict[str, int] = {}
    for word in given_list:
        if word in empty_dict:
            empty_dict[word] += 1
        else:
            empty_dict[word] = 1
    return empty_dict


def alphabetizer(given_list: list[str]) -> dict[str, list[str]]:
    """This function returns a dictionary where the keys are the first letters of the word and values are a list that contain all the words that begin with that specific key letter."""
    alphabetized_list: dict[str, list[str]] = {}
    used_letters: list[str] = []
    temp_first_letter: str = ""
    for word in given_list:
        temp_first_letter = word[0].lower()
        if temp_first_letter not in used_letters:
            letter_list: list[str] = []
            for word in given_list:
                if word[0].lower() == temp_first_letter:
                    letter_list.append(word)
                    alphabetized_list[temp_first_letter] = letter_list
        used_letters.append(temp_first_letter)
    return alphabetized_list


def update_attendance(given_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This function returns a dictionary updated with a day as the key and a value as the updated value."""
    new_list: list[str] = []
    if day in given_dict and (student not in given_dict[day]):
        given_dict[day].append(student)
    else:
        new_list.append(student)
        given_dict[day] = new_list
    return given_dict