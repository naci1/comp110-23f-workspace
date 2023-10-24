"""Combining two lists into a dictionary."""

__author__ = "730652828"

def zip(keys: list[str], values: list[int]) -> dict[str,int]:
    if len(keys) != len(values):
        return dict()
    else:
        new_dict: dict[str, int] = dict()
        # iterates through the list of keys.
        for i in range(len(keys)):
            new_dict[keys[i]] = values[i]
        return new_dict