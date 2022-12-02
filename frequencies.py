"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for each in items:
        each = str(each)
        if each in frequencies:
            frequencies[each] = frequencies[each] + 1

        else:
            frequencies[each] = 1;

    return frequencies


