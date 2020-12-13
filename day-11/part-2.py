# Day 11 Part 2

from typing import List

# Check up
def up(seats: List[str], i: int, j: int) -> str:
    a = i - 1
    while seats[a][j] == "." and a > 0:
        a -= 1
    return seats[a][j]
 
# Check down
def down(seats: List[str], i: int, j: int) -> str:
    a = i + 1
    while a < len(seats) - 1 and seats[a][j] == ".":
        a += 1
    return seats[a][j]

# Check left
def left(seats: List[str], i: int, j: int) -> str:    
    b = j - 1
    while b > 0 and seats[i][b] == ".":
        b -= 1
    return seats[i][b]

# Check right
def right(seats: List[str], i: int, j: int) -> str:
    b = j + 1
    while b < len(seats[0]) - 1 and seats[i][b] == ".":
        b += 1
    return seats[i][b]

# Check diag top left
def diagupleft(seats: List[str], i: int, j: int) -> str:
    a, b = i - 1, j - 1
    while a > 0 and b > 0 and seats[a][b] == ".":
        a -= 1
        b -= 1
    return seats[a][b]

# Check diag top right
def diagupright(seats: List[str], i: int, j: int) -> str:
    a, b = i - 1, j + 1
    while a > 0 and b < len(seats[0]) - 1 and\
        seats[a][b] == ".":
        a -= 1
        b += 1
    return seats[a][b]

# Check diag bottom left
def diagdownleft(seats: List[str], i: int, j: int) -> str:
    a, b = i + 1, j - 1
    while a < len(seats) - 1 and b > 0 and seats[a][b] == ".":
        a += 1
        b -= 1
    return seats[a][b]

# Check diag top right
def diagdownright(seats: List[str], i: int, j: int) -> str:
    a, b = i + 1, j + 1
    while a < len(seats) - 1 and b < len(seats[0]) - 1 and\
        seats[a][b] == ".":
        a += 1
        b += 1
    return seats[a][b]

def check_occ(seats:List[str], i: int, j: int) -> bool:
    """ Checks if currently occupied seat should become
        empty.
    """
    occupied_count = 0
   
    # Count how many visible seats are occupied
    occupied_count += (up(seats, i, j) == "#") +\
        (down(seats, i, j)          == "#") +\
        (left(seats, i, j)          == "#") +\
        (right(seats, i, j)         == "#") +\
        (diagupleft(seats, i, j)    == "#") +\
        (diagupright(seats, i, j)   == "#") +\
        (diagdownleft(seats, i, j)  == "#") +\
        (diagdownright(seats, i, j) == "#")

    return occupied_count >= 5

def check_empty(seats: List[str], i: int, j: int) -> bool:
    """ Checks if currently empty seat should become
        occupied.
    """
    # Check that all visible seats aren't occupied 
    return up(seats, i, j)          != "#" and\
        down(seats, i, j)           != "#" and\
        left(seats, i, j)           != "#" and\
        right(seats, i, j)          != "#" and\
        diagupleft(seats, i, j)     != "#" and\
        diagupright(seats, i, j)    != "#" and\
        diagdownleft(seats, i, j)   != "#" and\
        diagdownright(seats, i, j)  != "#"

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

    prev = []
    curr = seats
    
    # As long as seats are still changing, keep iterating
    while curr != prev:
        prev = curr
        curr = generate(curr)
  
        for row in curr:
            print(''.join(row))

    # Count occupied seats in final iteration
    return count(curr)

if __name__ == "__main__":
    #Parse input
    with open("input.txt", "r") as file:
        seats = [line.strip() for line in file]

    # Find final occupied seat count
    print("Final occupied seat count is", count_final_seats(seats))
