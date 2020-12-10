# Day 10 Part 1

from typing import List

def chain(adapters: List[int]) -> int:
    """ Takes a list of adapter voltages, then counts
        the difference between the outlet, each adapter,
        and the device.
    """
    # Sort it
    adapters = sorted(adapters)

    # Keep track of differences of 1 and 3
    one, three = 0, 0

    # Calculate each difference between adapters
    for i, adapter in enumerate(adapters):
        # Consider the difference between first adapter 
        # and outlet as well
        prior = adapters[i - 1] if i > 0 else 0
        diff = adapter - prior
        if diff == 3:
            three += 1
        if diff == 1:
            one += 1

    # Add device
    three += 1

    return one * three

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        adapters = [int(line) for line in file]

    # Calculate differences
    print("The number of 1-jolt and 3-jolt differences multiplied together is", chain(adapters))
