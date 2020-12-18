# Day 17 Part 1

from typing import List

def count_slice_neighbors(sl: List[List[str]], i: int, j: int, count_self: bool) -> int:
    """ Counts active neighbors in given slice """
    m, n = len(sl), len(sl[0])
    active = 0
    if i > 0:
        active += sl[i - 1][j]
    if i > 0 and j > 0:
        active += sl[i - 1][j - 1]
    if i > 0 and j < n - 1: 
        active += sl[i - 1][j + 1]
    if j > 0:
        active += sl[i][j - 1]
    if j < n - 1:
        active += sl[i][j + 1]
    if i < m - 1:
        active += sl[i + 1][j]
    if i < m - 1 and j > 0:
        active += sl[i + 1][j - 1]
    if i < m - 1 and j < n - 1:
        active += sl[i + 1][j + 1]
    if count_self:
        active += sl[i][j]
    return active

def num_active_neighbors(slices: List[List[List[str]]], slice_i: int, i: int, j: int)\
    -> int:
    """ Takes an array of slices representing a 3D space, a slice index
        indicating which slice we are currently looking at, and coordinates
        i and j indicating which cube in the slice we are looking at.
        Looks at the 26 surrounding locations and counts how many are 
        filled with active cubes.
    """
    active = 0
    
    # Neighbors in current slice
    active += count_slice_neighbors(slices[slice_i], i, j, False)
    
    # Neighbors in left slice
    if slice_i > 0:
        active += count_slice_neighbors(slices[slice_i - 1], i, j, True)

    # Neighbors in right slice
    if slice_i < len(slices) - 1:
        active += count_slice_neighbors(slices[slice_i + 1], i, j, True)

    return active

def boot(s: List[List[str]], cycles: int) -> int:
    """ Takes a single slice from a 3d plane and iterates
        given number of times according to these rules:
        1. If cube is active (#) and 2 or 3 of its neighbors
           are also active, it remains active. Otherwise,
           it becomes inactive.
        2. If a cube is inactive but 3 of its neighbors are 
           active, it becomes active.
        After given iterations, returns number of active cubes.
    """
    if not len(s) or not len(s[0]):
        return 0

    # Pad slice to the max size it will grow to (one perimeter
    # being added at each cycle)
    for i in range(len(s)):
        s[i] = [0] * cycles + s[i] + [0] * cycles

    for i in range(cycles):
        s.insert(0, [0] * len(s[i]))
        s.append([0] * len(s[i]))

    # Dimension of a slice
    m, n = len(s), len(s[0])

    # Array of all slices
    slices = [s]

    # Active Count
    total_active = 0

    # Add beginning active count
    for i in range(m):
        for j in range(n):
            total_active += s[i][j]

    # Iterate number of cycles
    for _ in range(cycles):
        # Add blank left and right slices to 3D space
        blank = [[0 for _ in range(n)] for _ in range(m)]
        slices.insert(0, blank[:])
        slices.append(blank[:])
      
        # All steps occur simultaneously
        new_slices = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(len(slices))]
        
        # Iterate through slices to update active and inactive cubes
        for i, sl in enumerate(slices):
            # Iterate through slice
            for a in range(m):
                for b in range(n):
                    # Count number of active neighbors
                    active = num_active_neighbors(slices, i, a, b)
                    # If cell is active but there aren't 2 or 3 active neighbors
                    if sl[a][b] and (active != 2 and active != 3):
                        new_slices[i][a][b] = 0
                        total_active -= 1
                    elif (not sl[a][b]) and (active == 3):
                        new_slices[i][a][b] = 1
                        total_active += 1
                    else:
                        new_slices[i][a][b] = sl[a][b]
        
        # Save new iteration    
        slices = new_slices

    return total_active

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [list(line.strip()) for line in file]

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] = 0 if lines[i][j] == "." else 1

    # Number of iterations desired
    cycles = 6

    # Count number of active cubes after n iterations
    print("There are {0} active cubes after {1} iterations".\
        format(boot(lines, cycles), cycles))
