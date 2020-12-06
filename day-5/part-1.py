# Day 5 Part 1

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

def get_max_code(seats: List[str], rows, cols) -> int:
    """ Convert all seats into seat codes, find max """
    max_code = 0
    max_seat = ""

    for seat in seats:
        seat_code = decode(seat, rows, cols)
        max_code = max(max_code, seat_code)
        #if seat_code > max_code:
        #    max_code = seat_code
        #    max_seat = seat

    return max_code
    #return (max_code, max_seat)

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Define plane size
    rows, cols = 128, 8

    # Get max seat code
    print("Max seat code is {0}".format(get_max_code(lines, rows, cols)))
