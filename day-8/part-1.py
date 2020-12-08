# Day 8 Part 1

from typing import List

def execute(instructions: List[str]) -> int:
    """ Executes all instructions in list until an 
        infinite loop is found. Returns value of
        accumulator at that point.
    """
    # Keep track of instructions that have been executed before 
    visited = [False for _ in range(len(instructions))]
    
    # Accumulator
    acc = 0

    # Execute instructions
    i = 0
    while i < len(instructions):
        # Check if instruction encountered before. If so, loop
        if visited[i]:
            return acc
        # Mark as visited
        visited[i] = True
        # Parse operation and argumnet
        op, arg = instructions[i].split(" ")
        arg = int(arg)
        # Execute operation
        if op == "jmp":
            i += arg - 1  # -1 to take into account the coming i+=1
        if op == "acc":
            print("here")
            acc += arg
        i += 1 

    # No loop found
    return -1

if __name__ == "__main__":

    # Parse input
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    # Execute instructions
    print("Accumulator contains {0} at loop".format(execute(lines)))
