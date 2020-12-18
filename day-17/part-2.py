# Day 17 Part 1

from typing import Dict, List, Tuple

def num_active_neighbors(cubes: Dict[Tuple[int], int], w: int,\
    x: int, y: int, z) -> int:
    """ Takes dictionary of 4-D cubes, checks all of its neighbors
        and sums how many active neighbors it has
    """
    active = 0
    # Check all neighbors (-1, 0, and 1)
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    curr = (w + i, x + j, y + k, z + l)
                    # Make sure not original cube
                    if curr in cubes and curr != (w, x, y, z):
                        active += cubes[curr]
    return active

def boot(cubes: Dict[Tuple[int], int], m: int, n: int, o: int, p: int, cycles: int) -> int:
    """ Takes a single slice from a 3d plane and iterates
        given number of times according to these rules:
        1. If cube is active (#) and 2 or 3 of its neighbors
           are also active, it remains active. Otherwise,
           it becomes inactive.
        2. If a cube is inactive but 3 of its neighbors are 
           active, it becomes active.
        After given iterations, returns number of active cubes.
    """
    # Active Count
    total_active = 0

    # Add beginning active count
    for i in range(m):
        for j in range(n):
            total_active += cubes[(i, j, 0, 0)]

    # Iterate number of cycles
    for h in range(1, cycles + 1):
        # Store new cubes
        new_cubes = {}

        # Iterate through map
        for i in range(-h, m + h):
            for j in range(-h, n + h):
                for k in range(-h, o + h):
                    for l in range(-h, p + h):
                        # Count number of active neighbors
                        active = num_active_neighbors(cubes, i, j, k, l)
                        
                        # Create cube if didn't exist before
                        if (i, j, k, l) not in cubes:
                            cubes[(i, j, k, l)] = 0
                        
                        # If cell is active but there aren't 2 or 3 active neighbors
                        if cubes[(i, j, k, l)] and (active != 2 and active != 3):
                            new_cubes[(i, j, k, l)] = 0
                            total_active -= 1
                        # If cell isn't active and has exactly 3 active neighbors
                        elif (not cubes[(i, j, k, l)]) and (active == 3):
                            new_cubes[(i, j, k, l)] = 1
                            total_active += 1
                        # Nothing changed
                        else:
                            new_cubes[(i, j, k, l)] = cubes[(i, j, k, l)]
        # Save new map 
        cubes = new_cubes

    return total_active

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [list(line.strip()) for line in file]
  
    # Store beginning dimensions
    m, n = len(lines), len(lines[0])
    
    # Store cubes as dictionary with coordinates as key
    cubes = {}
    for i in range(m):
        for j in range(n):
            cubes[(i, j, 0, 0)] = 0 if lines[i][j] == "." else 1
   
    # Number of iterations desired
    cycles = 6

    # Count number of active cubes after n iterations
    print("There are {0} active cubes after {1} iterations".\
        format(boot(cubes, m, n, 1, 1, cycles), cycles))
