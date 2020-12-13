# Day 12 Part 2

from typing import List, Union
import math

def parse_instruction(instruction: str, waypoint: List[int],
    lat: int, lon: int) -> Union[List[int], int, int]:
    """ Parses instruction and returns new coordinates and waypoint
    """
    # Parse instruction string
    action, val = instruction[:1], int(instruction[1:])

    # Rotate waypoint around ship
    if action == 'L':
        # Convert degree of rotation to radians
        rad = math.radians(val)
        y = math.sin(rad) * waypoint[1] + math.cos(rad) * waypoint[0]
        x = math.cos(rad) * waypoint[1] - math.sin(rad) * waypoint[0]
        waypoint = [round(y), round(x)]
    elif action == 'R':
        # Convert degree of rotation to radians
        rad = -math.radians(val)
        y = math.sin(rad) * waypoint[1] + math.cos(rad) * waypoint[0]
        x = math.cos(rad) * waypoint[1] - math.sin(rad) * waypoint[0]
        waypoint = [round(y), round(x)]
    # Move waypoint
    elif action == 'N':
        waypoint[0] += val
    elif action == 'S':
        waypoint[0] -= val
    elif action == 'E':
        waypoint[1] += val
    elif action == 'W':
        waypoint[1] -= val

    # Move ship coordinates to waypoint
    elif action == "F":
        for _ in range(val):
            lat += waypoint[0]
            lon += waypoint[1]

    # Invalid action
    else:
        print("Invalid action!")

    return (waypoint, lat, lon)

#parse_instruction('R90', [4, 10], 0, 0)
#parse_instruction('R90', [1, 0], 0, 0)
#parse_instruction('L90', [1, 0], 0, 0)
#parse_instruction('R90', [0,1], 0, 0)
#parse_instruction('L90', [0,1], 0, 0)

def move(instructions: List[str], waypoint: List[int]) -> int:
    """ Determines Manhattan distance after series of navigations
        are executed. 
    """
    # Determined relative to original position 
    lat, lon = 0, 0
    
    # Parse instructions
    for instruction in instructions:
        # Update ship's waypoint, direction, latitude, and longitude
        waypoint, lat, lon = parse_instruction(instruction, waypoint, lat, lon)
    
    return abs(lat) + abs(lon)

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        instructions = [line.strip() for line in file]
    
    # Define original direction
    waypoint = [1, 10]  # 1 unit north, 1 unit east

    # Navigate ship
    print("The Manhattan distance is", move(instructions, waypoint))
