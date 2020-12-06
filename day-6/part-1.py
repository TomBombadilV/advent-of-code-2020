# Day 6 Part 1

from typing import List

def count_yeses(answers: str) -> int:
    # Use set to ignore duplicates
    s = set()

    # Add all questions with a yes answer to the set
    for c in answers:
        s.add(c)
   
    # Count number of questions with yes answer
    return len(s)

def sum_groups(groups: List[str]) -> int:
    # Sum yes count for all groups
    res = 0
    for group in groups:
        res += count_yeses(group)

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
                s += line.strip()
        groups.append(s)

    # Sum all yes counts from each group
    print("Yeses sum to {0}".format(sum_groups(groups)))
