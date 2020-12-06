# Day 4 Part 1

import re
from typing import List

def valid_field(key: str, value: str) -> bool:
    """ Check further validations """        
   
    if key == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    elif key == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020
    elif key == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030
    elif key == 'hgt':
        val = re.match("(\d+)(cm|in)", value)
        if val.group(2) == "cm":
            return int(val.group(1)) >= 150 and int(val.group(1)) <= 193
        else:
            return int(val.group(1)) >= 59 and int(val.group(1)) <= 76
    else:  # If key is hcl, ecl, or pid, no further validation required
        #print(key, ":", value)
        return True

def is_valid(passport: str, exp_fields: List[str]) -> bool:
    """ Tests whether a passport is valid (whether it contains
        all expected fields)
    """
    for field in exp_fields:
        # Search for current field pattern
        res = re.search(field, passport)
        # Pass key and value into valid_field function
        if not res or not valid_field(res.group(1), res.group(2)):
            #print(field, "failed")
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
                passports.append(s + " ")
                s = ""
            else:
                s += line
    # Add last string
    passports.append(s)

    # Define expected fields and their expected values
    exp_fields = [
        "(byr):(\d{4})\s", 
        "(iyr):(\d{4})\s",
        "(eyr):(\d{4})\s",
        "(hgt):(\d+(in|cm))\s", 
        "(hcl):(#(\w|\d){6})\s", 
        "(ecl):(amb|blu|brn|gry|grn|hzl|oth)\s", 
        "(pid):(\d{9})\s"
    ]

    print("{0} valid passports".format(count_valid_passports(passports, exp_fields)))
