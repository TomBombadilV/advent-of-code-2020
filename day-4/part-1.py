# Day 4 Part 1

import re
from typing import List

def is_valid(passport: str, exp_fields: List[str]) -> bool:
    """ Tests whether a passport is valid (whether it contains
        all expected fields)
    """
    for field in exp_fields:
        pattern = field + ":"
        if not re.search(pattern, passport):
            return False
    
    return True

def count_valid_passports(passports: List[str], exp_fields: List[str]) -> int:
    """ Counts valid passports (passports with all expected fields) """ 
    count = 0

    for passport in passports:
        count += is_valid(passport, exp_fields)

    return count

if __name__ == "__main__":
   
    passports = []

    # Parse input
    with open("input.txt", "r") as file:
        s = ""
        for line in file:
            # Passport delimeted by blank line
            if line == "\n":
                passports.append(s)
                s = ""
            else:
                s += line.strip()
    # Add last string
    passports.append(s)

    # Define expected fields
    exp_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    print("{0} valid passports".format(count_valid_passports(passports, exp_fields)))
