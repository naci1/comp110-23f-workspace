"""Test my zip function."""

__author__ = "730652828"

from lessons.zip import zip


def test_lists_diff_length() -> None:
    """Returns an empty dictionary if the length of two lists are different(Use case)."""
    list_1: list[str] = ["cats", "dogs", "pineappples"]
    list_2: list[int] = [4, 5, 8, 10]
    assert zip(list_1, list_2) == dict()


def test_lists_empty_elems() -> None:
    """Returns an empty dictionary if the length of both lists are 0(Edge case)."""
    list_1: list[str] = []
    list_2: list[int] = []
    assert zip(list_1, list_2) == dict()


def test_same_size_lists() -> None:
    """The function zip(["a","b","c"], [4,5,6]) should return {"a": 4, "b": 5, "c": 6}."""
    list_1: list[str] = ["a", "b", "c"]
    list_2: list[int] = [4, 5, 6]
    assert zip(list_1, list_2) == {"a": 4, "b": 5, "c": 6}