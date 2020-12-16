# Day 16 Part 2

from part1 import parse_valid_fields
from typing import Dict, List

def parse_field_ranges(fields: List[str])\
    -> Dict[str, List[int]]:
    """ Takes strings of fields and their valid ranges,
        puts them in dictionary
    """
    # Dictionary of field names and ranges
    dic = {}
    
    for field in fields:
        # Parse field sections to get ranges
        name, ranges = field.split(": ")
        range_a, range_b = ranges.split(" or ")
        a_min, a_max = range_a.split("-")
        b_min, b_max = range_b.split("-")

        # Save name and range in dictionary as array of four values
        # (minA, maxA, minB, maxB)
        dic[name] = [int(a_min), int(a_max), int(b_min), int(b_max)] 

    return dic

def remove_invalid_tickets(valid: List[bool], tickets: List[List[int]])\
    -> List[List[int]]:
    """ Takes a list of tickets and removes the invalid ones """
    # Keep track of valid tickets
    valid_tickets = []
    
    # Iterate through all values on all tickets, summing all
    # invalid values encountered
    for ticket in tickets:
        isValid = True
        # Make sure ticket is valid
        for val in ticket:
            if not valid[val]:
                isValid = False
        # If no invalid fields found, add to validTickets array
        if isValid:
            valid_tickets.append(ticket)

    return valid_tickets


def assign_fields(my_ticket: List[int], tickets: List[List[int]],\
    range_dic: Dict[str, int]) -> int:
    """ Takes a list of tickets and fields and determines the order of 
        the fields
    """
    # Store assignments for each index on the ticket
    field_assignment = ["" for key in range_dic]

    # Keep track of unassigned fields
    remaining_fields = [key for key in range_dic]

    # Repeat until all fields are assigned (if this is possible, 
    # it must be doable within "number of fields" iterations)
    for _ in range(len(field_assignment)):
        
        # Iterate through each index, ticket by ticket
        for j in range(len(my_ticket)):
            # Keep track of fields that current index could possibly be
            possible_fields = remaining_fields[:]

            for i in range(len(tickets)):
                val = tickets[i][j]
                # For each possible field
                k = 0
                while k < len(possible_fields):
                    key = possible_fields[k]
                    # Check if current ticket value exists within that range
                    if not((val >= range_dic[key][0] and val <= range_dic[key][1])\
                        or (val >= range_dic[key][2] and val <= range_dic[key][3])):
                        # If not, remove that field
                        del possible_fields[k]
                    else:
                        k += 1
            
            # If reduced to one possible field, assign it! And remove it from
            # unassigned fields array
            if len(possible_fields) == 1:
                remaining_fields.remove(possible_fields[0])
                field_assignment[j] = possible_fields[0]

    return field_assignment

def departure_field_product(field_assignment: List[str], my_ticket: List[int]) -> int:
    """ Takes array indicating which field each index is and a ticket. 
        Finds all values for fields regarding departure, and multiplies them.
    """
    prod = 1
    for i, field in enumerate(field_assignment):
        if field[:9] == "departure":
            prod *= my_ticket[i]
    return prod

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
    
        # Throw away newline and "your ticket" header
        file.readline()

        # Get my ticket        
        my_ticket = file.readline().strip().split(",")
        my_ticket = [int(val) for val in my_ticket]
        
        # Throw away newline and "nearby tickets" header
        file.readline()
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

    # Remove invalid tickets 
    tickets = remove_invalid_tickets(valid, tickets)

    # Convert fields into dictionary of ranges
    range_dic = parse_field_ranges(fields)

    # Get field assignment
    field_assignments = assign_fields(my_ticket, tickets, range_dic)

    # Calculate product
    print("The product of six departure fields is", departure_field_product(field_assignments, my_ticket)) 
