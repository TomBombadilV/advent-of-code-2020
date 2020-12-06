# Day 2 Part 2

from typing import List

def is_valid(rule: str, password: str) -> bool:
    """ Determines whether a password is valid based
        on given rule, which indicates two indices and a 
        character. Exactly one of these indices should contain
        the indicated character.
    """

    # Parse rule
    indices, char = rule.split(" ")
    i, j = indices.split("-")
    i, j = int(i) - 1, int(j) - 1  # Convert from 1- to 0-based indexing

    # Use XOR to check that only one is the char
    return (password[i] == char) ^ (password[j] == char)

def count_valid_passwords(lines: List[str]) -> int:
    """ Counts number of valid passwords from lines of
        rules and passwords
    """
    # Keep track of valid passwords
    count = 0

    # Check all passwords against their rule
    for line in lines:
        rule, password = line.split(": ")
        count += is_valid(rule, password)

    return count

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]
    
    # Count number of valid passwords
    print("{0} valid passwords".format(count_valid_passwords(lines)))
