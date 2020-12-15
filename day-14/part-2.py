# Day 14 Part 2

from collections import defaultdict
from typing import List, Tuple

import re

def mask_address(bitmask: str, addr: int) -> int:
    """ Takes an address and masks it with bitmask """
    # Store all corresponding addresses
    addrs = [0]

    # Iterate through bitmask
    for i in range(len(bitmask)):
        # Want to iterate bitmask from right to left
        # Add 1 to beginning of each bitstring in address array
        if bitmask[-(i + 1)] == "1":
            addrs = [a + (1 << i) for a in addrs]
        # Add 1 AND 0 to beginning of each bitstring in array
        elif bitmask[-(i + 1)] == "X":
            # Add 0
            old_addrs = addrs
            # Add 1
            addrs = [a + (1 << i) for a in addrs]
            # Combine
            addrs += old_addrs
        # Add current bit to all addresses in array
        else:
            addrs = [a + ((addr & 1) << i) for a in addrs]
        # Move to next bit in address
        addr >>= 1

    # If address is longer than bitstring, add the rest of the address` 
    if addr:
        addrs = [a + (addr << len(bitmask)) for a in addrs]

    return addrs

def parse(lines: List[str]) -> int:
    """ Takes a list of bitmasks and entries into memory, then
        sums them all.
    """
    # Dictionary of memory locations and their values
    dic = defaultdict(int)
    
    mask = ""
    
    for line in lines:
        print(line)
        if line[:4] == "mask":
            # Get new bitmask
            mask = line.split(" = ")[1]
        else:
            # Parse line to get memory location and number
            match = re.match("mem\[(\d+)\] = (\d+)", line) 
            loc, val = int(match[1]), int(match[2])
            
            # Apply current bitmask to address. Take resulting
            # array of addresses and add to dictionary
            addrs = mask_address(mask, loc)
            for addr in addrs:
                dic[addr] = val
    
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
