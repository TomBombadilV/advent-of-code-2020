# Day 3 Part 1

from typing import List

def count_trees(M: List[str], right: int, down: int) -> int:
    """ Counts number of trees encountered on (repeating) map
        by repeatedly traversing it to the right and down by 
        the given numbers
    """
    # If map is empty or slope never goes down, nothing will happen
    if len(M) == 0 or down == 0:
        return 0

    # Initialize stuff
    m, n = len(M), len(M[0])  # Map dimensions
    i, j = 0, 0  # Current location
    trees = 0  # Trees encountered

    # While we haven' run off the slope yet lol
    while i < m:
        # If tree encountered, count it
        if M[i][j] == "#":
            trees += 1

        # Move down and to the right
        i += down
        j = (j + right) % n  # Mod because map repeats to the right

    return trees

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Define right and down params
    right, down = 3, 1

    # Count trees encountered
    print("{0} trees encountered".format(count_trees(lines, right, down)))
