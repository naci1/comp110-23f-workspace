"""Testing for the functions defined in dictionary.py."""

__author__ = "730652828"

from dictionary import invert, favorite_color, count, alphabetizer, update_attendance

import pytest

"""The test cases below test for the function "invert"."""


def test_empty_dict() -> None:
    """If the given_dict is empty, invert(given_list) should return {}(edge case)."""
    given_dict: dict[str, str] = {}
    assert invert(given_dict) == dict()


def test_dict_unique_values() -> None:
    """If the given_dict has unique values, it should invert the dictionary(use case)."""
    given_dict: dict[str, str] = {'a': 'l', 'b': 'k', 'c': 'd'}
    assert invert(given_dict) == {'l': 'a', 'k': 'b', 'd': 'c'}


def test_dict_nonunique_values() -> None:
    """If the given_dict has at least one pair of non-unique values, it should not invert the dictionary and instead raise a Key error(use case)."""
    given_dict: dict[str, str] = {'k': 'lol', 'm': 'lol'}
    with pytest.raises(KeyError):
        invert(given_dict)


"""The test_cases below test for the function "favorite_colors"."""


def test_empty_dict_for_favorite() -> None:
    """If the given_dict is empty, favorite_color(given_dict) should return an empty string(edge case)."""
    given_dict: dict[str, str] = {} 
    assert favorite_color(given_dict) == ""


def test_one_color_appeares_most() -> None:
    """If the given_dict has only value that appears the most, favorite_color(given_dict) should return that value(use_case)."""
    given_dict: dict[str, str] = {'Marc': 'yellow', 'Narasimha': 'yellow', 'John': 'blue'}
    word_returned: str = 'yellow'
    assert favorite_color(given_dict) == word_returned


def test_multiple_color_appeares_most() -> None:
    """If the given_dict has multiple values thta appear the most, favorite_color(given_dict) should return the color that appeared first(use case)."""
    word_returned: str = ""
    given_dict: dict[str, str] = {'Marc': 'yellow', 'Narasimha': 'red', 'Michael': 'yellow', 'Andreas': 'red'}
    word_returned = 'yellow'
    assert favorite_color(given_dict) == word_returned


"""The test_cases below are for the function "count"."""


def test_every_element_in_list_same() -> None:
    """If the given_list has all the same values, count should just produce a dict with one key and value pair(edge case because we would not expect a list to have values that are all the same)."""
    returned_dict: dict[str, int] = {}
    given_list: list[str] = ['car', 'car', 'car', 'car', 'car']
    returned_dict = {'car': 5}
    assert count(given_list) == returned_dict


def test_every_element_different_in_list() -> None:
    """If the given_list has all unique values, the number of key value pairs returned by count should be equal to the length of the list(use case)."""
    returned_dict: dict[str, int] = {}
    given_list: list[str] = ['car', 'dog', 'log']
    returned_dict = {'car': 1, 'dog': 1, 'log': 1}
    assert count(given_list) == returned_dict


def test_repeated_elements_in_list() -> None:
    """If the given_list has repeated values, then count should return a key value pair such that one value is greater than 1(use case)."""
    returned_dict: dict[str, int] = {}
    given_list: list[str] = ['car', 'dog', 'log', 'car']
    returned_dict = {'car': 2, 'dog': 1, 'log': 1}
    assert count(given_list) == returned_dict


"""The test_cases below test for the function "alphabetizer"."""


def test_empty_list() -> None:
    """If the given_list is empty, then alphabetizer should return an empty dictionary(edge case)."""
    returned_dict: dict[str, str[list]] = {}
    given_list: list[str] = []
    returned_dict = {}
    assert alphabetizer(given_list) == returned_dict


def test_multiple_elements_start_with_same_letter() -> None:
    """If the given_list has multiple elements that start with the same letter, the value list for a key has more than one element(use case)."""
    returned_dict: dict[str, str[list]] = {}
    given_list: list[str] = ['cat', 'dog', 'class']
    returned_dict = {'c': ['cat', 'class'], 'd': ['dog']}
    assert alphabetizer(given_list) == returned_dict


def test_at_least_one_value_in_list_upper_cased() -> None:
    """If the given_list has at least one value that is upper cased, then alphabetizer should still add that value into the value list UNALPHABETIZED(use case)."""
    returned_dict: dict[str, str[list]] = {}
    given_list: list[str] = ['Cat', 'log', 'Class', 'Lid']
    returned_dict = {'c': ['Cat', 'Class'], 'l': ['log', 'Lid']}
    assert alphabetizer(given_list) == returned_dict


"""The test cases below test for the function "update_attendance"."""


def test_empty_dict_and_day_student_empty() -> None:
    """If the given_dict is empty and student = "" and day = "", update_attendance should just return the given_dict(edge case)."""
    returned_dict: dict[str, list[str]] = {}
    student: str = ""
    day: str = ""
    assert update_attendance(returned_dict, day, student) == returned_dict
  

def test_empty_dict_and_day_student_non_empty() -> None:
    """If the given_dict is empty and student and day are non_empty, update_attendance should return a dictionary with day as the key and student(as a list) as the value(use case)."""
    returned_dict: dict[str, list[str]] = {}
    returned_value_list = []
    student: str = "Andreas"
    day: str = "Monday"
    returned_value_list.append(student)
    returned_dict = {day: returned_value_list}
    assert update_attendance(returned_dict, day, student) == returned_dict


def test_non_empty_dict_and_day_student_non_empty() -> None:
    """If the given_dict is non_empty and student and day are non_empty, update_attendance should return a dictionary with day as a key and value_list appended with the student value(use case)."""
    returned_dict: dict[str, list[str]] = {'Monday': ['Andreas', 'Bjorn'], 'Tuesday': ['Hafthor']}
    day: str = "Monday"
    student: str = "Felix"
    returned_dict[day].append(student)
    assert update_attendance(returned_dict, day, student) == returned_dict