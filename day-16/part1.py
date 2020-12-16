# Day 16 Part 1

from typing import List

def parse_valid_fields(fields: List[str], max_val: int) -> List[bool]:
    """ Takes strings of fields and their valid ranges,
        and turns them into an array, where arr[value]
        tells whether that value is valid or not
    """
    # Boolean array keeping track of valid values
    valid = [False] * max_val

    for field in fields:
        # Parse field sections to get ranges
        _, ranges = field.split(": ")
        range_a, range_b = ranges.split(" or ")
        a_min, a_max = range_a.split("-")
        b_min, b_max = range_b.split("-")

        # Iterate through both ranges to preserve valid values
        for i in range(int(a_min), int(a_max) + 1):
            valid[i] = True
        for i in range(int(b_min), int(b_max) + 1):
            valid[i] = True

    return valid


def error_rate(valid: List[bool], tickets: List[List[int]]) -> int:
    """ Takes an array of valid indices and a list of tickets,
        scans the tickets to check for fields that are invalid.
    """
    # Keep track of ticket scanning error rate (sum of all invalid
    # fields)
    rate = 0

    # Iterate through all values on all tickets, summing all
    # invalid values encountered
    for ticket in tickets:
        for val in ticket:
            if not valid[val]:
                rate += val
    
    return rate

if __name__ == "__main__":
    # Keep track of fields and tickets
    fields = []
    tickets = []
    
    # Parse input
    with open("input.txt", "r") as file:
        # Get field lines
        line = file.readline()
        while line != "\n":
            fields.append(line.strip())
            line = file.readline()
    
        # Throw away your ticket lines and header line
        for _ in range(4):
            file.readline()

        # Get ticket lines
        line = file.readline()
        while line:
            # Convert into array of ints
            ticket = line.strip().split(",")
            ticket = [int(val) for val in ticket]
            tickets.append(ticket)
            line = file.readline()

    # Convert ranges into array of bools
    valid = parse_valid_fields(fields, 1000)

    # Calculate scanning error rate
    print("The error scanning rate is", error_rate(valid, tickets))
