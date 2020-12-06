# Day 6 Part 1

from collections import Counter
from typing import List

def count_parity(votes: List[str]) -> int:
    """ Counts how many questions every single
        person in the group voted yes for
    """
    # Count all of the votes cast
    dic = Counter()
    for vote in votes:
        for c in vote:
            dic[c] += 1

    # Count number of people in group
    num_people = len(votes)

    # Check all keys in dictionary that have 
    # a count equal to the number of people in 
    # the group
    parity_count = 0
    for key in dic:
        if dic[key] == num_people:
            parity_count += 1

    return parity_count

def sum_parities(groups: List[str]) -> int:
    """ Sums parity counts across all groups """
    res = 0
    for group in groups:
        votes = group.split()
        res += count_parity(votes)

    return res

if __name__ == "__main__":
    # Parse Input
    groups = []
    s = ""
    with open("input.txt", "r") as file:
        for line in file:
            if line == "\n":
                groups.append(s)
                s = ""
            else:
                s += line.strip() + " "
        groups.append(s)
    
    # Count parity votes across all groups
    print("{0} votes summed".format(sum_parities(groups)))
