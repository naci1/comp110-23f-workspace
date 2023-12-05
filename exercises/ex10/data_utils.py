from csv import DictReader

"""Dictionary related utility functions."""

__author__ = "730652828"

# Define your functions below

"""Working with CSV Data."""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Providing data for the first n rows of a table."""
    dict_to_be_returned: dict[str, list[str]] = {}
    for key in table:
        empty_list: list[str] = []
        value_we_are_at: int = 0
        for string in table[key]:
            if(value_we_are_at < num_rows):
                empty_list.append(string)
            value_we_are_at += 1
        dict_to_be_returned[key] = empty_list
    return dict_to_be_returned


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Selecting names of a column that we wish to copy to a new dictionary."""
    dict_to_be_returned: dict[str, list[str]] = {}
    for value in col_names:
        if value in table:
            dict_to_be_returned[value] = table[value]
    return dict_to_be_returned


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables and returns a new table."""
    dict_to_be_returned: dict[str, list[str]] = {}
    for key in table_1:
        dict_to_be_returned[key] = table_1[key]
    for key in table_2:
        if key in dict_to_be_returned:
            dict_to_be_returned[key] += table_2[key]
        else:
            dict_to_be_returned[key] = table_2[key]
    return dict_to_be_returned


def count(data: list[str]) -> dict[str, int]:
    """Make a dict with the keys as unique string values from the "data" and int as the number of times the value occured."""
    empty_dict: dict[str, int] = {}
    for value in data:
        if value in empty_dict:
            empty_dict[value] += 1
        else:
            empty_dict[value] = 1
    return empty_dict