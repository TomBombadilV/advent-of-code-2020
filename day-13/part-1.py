# Day 13 Part 1

import sys
from typing import List

def next_bus(timestamp: int, buses: List[int]) -> int:
    """ Takes the starting timestamp and finds the next bus
        you can depart on. Buses all leave at timestamp 0, then
        take the given amount of time to return and leave again.
    """
    # Make sure stuff is valid
    if len(buses) == 0 or timestamp < 0:
        return -1

    # Keep track of minimum waiting time and corresponding bus
    min_time, min_bus = sys.maxsize, None

    for bus in buses:
        # Use ceiling division to find multiple of bus that is 
        # greater than timestamp
        time = -(-timestamp // bus) * bus
        waiting_time = time - timestamp
        
        # Update min waiting time 
        if waiting_time < min_time:
            min_time = waiting_time
            min_bus = bus

    return min_time * min_bus

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        timestamp = int(file.readline())
        buses = file.readline().split(',')
        buses = [int(bus) for bus in buses if bus != "x"]

    # Find next bus
    print("The next bus and the waiting time multiplied is", next_bus(timestamp, buses))
