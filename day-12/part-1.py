# Day 12 Part I

from typing import List, Union
import math

def parse_instruction(instruction: str, direction: int, lat: int, lon: int)\
    -> Union[int, int, int]:
    """ Parses instruction and returns new direction (as 
        degrees rotation clockwise from North) and coordinates.
    """
    # Parse instruction string
    action, val = instruction[:1], int(instruction[1:])

    # Only L and R instructions change the ship's direction
    if action == 'L':
        direction = (direction - val) % 360
    elif action == 'R':
        direction = (direction + val) % 360
    
    # All other direction change coordinates of ship
    elif action == 'N':
        lat += val
    elif action == 'S':
        lat -= val
    elif action == 'E':
        lon += val
    elif action == 'W':
        lon -= val

    # Forward moves the ship based on its current direction
    elif action == "F":
        # Convert direction in degrees to radians
        rad = math.radians(direction)
        lat += int(math.cos(rad) * val)
        lon += int(math.sin(rad) * val)

    # Invalid action
    else:
        print("Invalid action!")

    return (direction, lat, lon)

#print(parse_instruction('F5', 0, 0, 0))
#print(parse_instruction('F5', 90, 0 ,0))
#print(parse_instruction('F5', 180, 0, 0)) 
#print(parse_instruction('F5', 270, 0 ,0))

def move(instructions: List[str], direction: int) -> int:
    """ Determines Manhattan distance after series of navigations
        are executed. 
    """
    # Determined relative to original position 
    lat, lon = 0, 0
    
    # Parse instructions
    for instruction in instructions:
        # Update ship's direction, latitude, and longitude
        direction, lat, lon = parse_instruction(instruction, direction, lat, lon)
    
    return abs(lat) + abs(lon)

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        instructions = [line.strip() for line in file]
    
    # Define original direction
    direction = 90  # Originally facing east 

    # Navigate ship
    print("The Manhattan distance is", move(instructions, direction))
