# Day 2 Part 1

from typing import List

def check_password(rule: str, password: str) -> bool:
    """ Checks validity of a password based on a rule
        which determines the upper and lower count of a 
        particular character that the password can have
    """
    # Parse password rule
    limit, char = rule.split(" ")
    low, high = limit.split("-")

    # Count instances of characters in password
    count = password.count(char)
    
    # Check against limits
    return count >= int(low) and count <= int(high)

def count_valid_passwords(lines: List[str]):
    """ Counts the number of valid passwords by parsing
        lines containing a rule and a password
    """
    count = 0
    
    # Parse line by splitting rule and password, then checking its validity
    for line in lines:
        rule, password = line.split(": ")
        count += check_password(rule, password)

    return count

if __name__ == "__main__":
    # Parse file
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]
    
    # Count valid passwords
    print("{0} valid passwords".format(count_valid_passwords(lines)))
