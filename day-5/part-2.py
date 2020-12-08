# Day 5 Part 2

from typing import List

def decode(seat: str, rows: int, cols: int) -> int:
    """ Converts a seat into its seat code """
    # Keep track of current seat window
    row_left, row_right = 0, rows - 1
    col_left, col_right = 0, cols - 1

    # Iterate through seat string, updating current seat window
    for c in seat:
        if c == "F":  # Move window to front half
            row_right = (row_left + row_right + 1) // 2
        elif c == "B":  # Move window to back half
            row_left = (row_left + row_right + 1) // 2
        elif c == "L":  # Move window to left half
            col_right = (col_left + col_right + 1) // 2
        elif c == "R":  # Move window to right half
            col_left = (col_left + col_right + 1) // 2
        else:
            print("Invalid letter")
            return -1

    # Convert to seast code
    return row_left * 8 + col_left

def missing_seat(seats: List[str], rows: int, cols: int) -> int:
    """ Finds missing seat that is not from beginning or end """
    # Array marking whether seat code has been encountered
    found = [False for _ in range(rows * cols)]
    
    # Decode each seat and mark it as encountered
    for seat in seats:
        code = decode(seat, rows, cols)
        found[code] = True
    
    # Move past beginning nonexistent seats
    i = 0
    while found[i] == False:
        i += 1

    # Iterate until you find a missing seat
    while found[i] == True:
        i += 1

    return i

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Define plane size
    rows, cols = 128, 8

    # Get max seat code
    print("Missing seat code is {0}".format(missing_seat(lines, rows, cols)))
