# Day 15 Part 1

from typing import List

def number_suffix(n: int) -> str:
    return "st" if n % 10 == 1 else "th"

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

    while i < len(arr) - 1:
        curr = arr[i]
        dic[curr] = i
        i += 1

    curr = arr[i]

    while i < n - 1:
        if curr not in dic:
            dic[curr] = i
            curr = 0
        else:
            prev = dic[curr]
            dic[curr] = i
            diff = i - prev
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
