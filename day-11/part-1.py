# Day 11 Part 1

from typing import List

def check_occ(seats:List[str], i: int, j: int) -> bool:
    """ Checks if currently occupied seat should become
        empty.
    """
    occupied_count = (seats[i - 1][j] == "#") +\
        (seats[i - 1][j - 1] == "#") +\
        (seats[i - 1][j + 1] == "#") +\
        (seats[i + 1][j]     == "#") +\
        (seats[i + 1][j - 1] == "#") +\
        (seats[i + 1][j + 1] == "#") +\
        (seats[i][j - 1]     == "#") +\
        (seats[i][j + 1]     == "#")

    return occupied_count >= 4

def check_empty(seats: List[str], i: int, j: int) -> bool:
    """ Checks if currently empty seat should become
        occupied.
    """
    all_empty = seats[i - 1][j]  != "#" and\
        seats[i - 1][j - 1] != "#" and\
        seats[i - 1][j + 1] != "#" and\
        seats[i + 1][j]     != "#" and\
        seats[i + 1][j - 1] != "#" and\
        seats[i + 1][j + 1] != "#" and\
        seats[i][j - 1]     != "#" and\
        seats[i][j + 1]     != "#" 

    return all_empty

def generate(seats: List[str]) -> List[str]:
    """ Takes a seating map with empty seats (L), filled
        seats (#), and floor spaces (.). Applies the rules:
        1. If seat is empty with no adjacent occupied seats, 
           seat becomes filled.
        2. If seat is occupied and 4+ seats adjacent (LRUD
           or diag) are occupied, seat becomes empty.
        Returns state after rules are applied.
    """
    m = len(seats)
    n = len(seats[0]) if m else 0

    regen = [["." for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if seats[i][j] == "L":
                regen[i][j] = "#" if check_empty(seats, i, j) else "L"
            if seats[i][j] == "#":
                regen[i][j] = "L" if check_occ(seats, i, j) else "#"
 
    for i in range(m):
        regen[i] = "".join(regen[i])

    return regen

def count(seats: List[str]) -> int:
    """ Counts number of occupied seats """
    # Map dimensions
    m = len(seats)
    n = len(seats[0]) if m else 0
    
    count = 0
    
    # Count locations filled with "#"
    for i in range(m):
        for j in range(n):
            if seats[i][j] == "#":
                count += 1

    return count

def count_final_seats(seats: List[str]) -> int:
    # Map dimensions
    m = len(seats)
    n  = len(seats[0]) if m else 0

    # Pad seat map so we don't need to bother about corners/edges
    seats = ["." + row + "." for row in seats]
    seats.insert(0, "." * (n + 2))
    seats.append("." * (n + 2))

    # Calculate first iteration
    prev = seats
    curr = generate(seats)

    # As long as seats are still changing, keep iterating
    while curr != prev:
        prev = curr
        curr = generate(curr)
    # Count occupied seats in final iteration
    return count(curr)

if __name__ == "__main__":
    #Parse input
    with open("input.txt", "r") as file:
        seats = [line.strip() for line in file]

    # Find final occupied seat count
    print("Final occupied seat count is", count_final_seats(seats))
