# Day 15 Part 1

from typing import List

def number_suffix(n: int) -> str:
    """ Returns proper suffix (ex: 1 -> 1st, 2 -> 2nd)"""
    dig = n % 10
    if dig == 1:
        return "st"
    elif dig == 2:
        return "nd"
    elif dig == 3:
        return "rd"
    else:
        return "th"

def play(arr: List[int], n: int) -> int:
    """ Takes an array of numbers, plays game according
        to the following rules:
        1. If first time the previous number was encountered,
           player says 0
        2. If encountered before, say how many turns ago it
           was previously spoken.
    """
    dic = {}
    curr, i = 0, 0

    # Add all but last starting number to dictionary
    while i < len(arr) - 1:
        curr = arr[i]
        dic[curr] = i
        i += 1

    # Move to last starting number
    curr = arr[i]

    # Iterate to nth move
    while i < n - 1:
        # Check if previous number has been spoken
        if curr not in dic:
            dic[curr] = i
            curr = 0
        # If not
        else:
            # Get last index and calculate difference
            diff = i - dic[curr]
            dic[curr] = i  # Update with new index
            curr = diff
        i += 1

    return curr

if __name__ == "__main__":
    # Define known cases
    cases = [
        #([0, 3, 6], 0),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836)
    ]

    # Index desired
    n = 2020
    #n = 10

    # Test known cases
    for arr, expected in cases:
        res = play(arr, n)
        print("Passed" if res == expected else \
            "Failed with {0} expected {1}".format(res, expected))

    # Define numbers
    arr = [8, 13, 1, 0, 18, 9]

    # Calculate 2020th number spoken
    print("The {0}{1} number spoken is {2}".\
        format(n, number_suffix(n), play(arr, n)))
