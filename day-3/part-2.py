# Day 3 Part 2

from part1 import count_trees
from typing import List, Tuple

def tree_product(M: List[str], slopes: List[Tuple[int]]) -> int:
    product = 1

    for slope in slopes:
        right, down = slope
        product *= count_trees(M, right, down)
    
    return product

def main():
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Define right and down params
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    # Count trees encountered
    print("{0} trees encountered".format(tree_product(lines, slopes)))

main()
