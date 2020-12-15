# Day 14 Part 1

from collections import defaultdict
from typing import List, Tuple

import re

def mask_num(bitmask: str, num: int) -> int:
    """ Takes a number and masks it with bitmask """
    # Iterate through bitmask
    for i in range(len(bitmask)):
        # Want to iterate bitmask from right to left
        if bitmask[-(i + 1)] == "0":
            num &= ~(1 << i)  # Set ith bit to 0
        elif bitmask[-(i + 1)] == "1":
            num |= (1 << i)  # Set ith bit to n
        else:
            pass
    return num

def parse(lines: List[str]) -> int:
    """ Takes a list of bitmasks and entries into memory, then
        sums them all.
    """
    # Dictionary of memory locations and their values
    dic = defaultdict(int)
    
    mask = ""
    
    for line in lines:
        if line[:4] == "mask":
            # Get new bitmask
            mask = line.split(" = ")[1]
        else:
            # Parse line to get memory location and number
            match = re.match("mem\[(\d+)\] = (\d+)", line) 
            loc, val = int(match[1]), int(match[2])
            # Apply current bitmask to number and add to dictionary
            dic[loc] = mask_num(mask, val)
    
    # Sum up all filled memory locations
    res = 0
    for key in dic:
        res += dic[key]

    return res
    
if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Find sum of all masked memory entries
    print("The sum is", parse(lines))
