# Day 8 Part 2

from typing import List, Tuple

def find_loop(instructions: List[str], visited: List[bool], i: int, acc: int) -> Tuple[bool, int]:
    """ Starting at given instruction, checks if a loop will be
        encountered.
    """
    curr_visited = visited[:]
    
    # Execute instructions
    while i < len(instructions):
        
        # Check if instruction encountered before. If so, loop
        if curr_visited[i]:
            return (True, -1)
        
        # Mark as visited
        curr_visited[i] = True
        
        # Parse operation and argumnet
        op, arg = instructions[i].split(" ")
        arg = int(arg)
        
        # Execute operation
        if op == "jmp":
            i += arg - 1  # -1 to take into account the coming i+=1
        if op == "acc":
            acc += arg 
        i += 1  

    return (False, acc)

def execute(instructions: List[str]) -> int:
    """ For all nops, execute as though it was switched to jump.
        If finds loop, ignore and continue. For all jumps, execute
        as though nop.
    """
   
    # Keep track of instructions that have been executed before
    visited = [False for _ in range(len(instructions))]

    # Accumulator
    acc = 0

    # Execute instructions
    i = 0
    while i < len(instructions):
        
        # Parse operation and argumnet
        op, arg = instructions[i].split(" ")
        arg = int(arg)
        
        # Execute operation
        if op == "jmp":
            # Try switching to nop
            has_loop, final_acc = find_loop(instructions, visited, i + 1, acc)
            
            # If that eliminates cycle, return final acc value
            if not has_loop:
                return final_acc
            # If not, continue as usual
            else:
                i += arg - 1  # -1 to take into account the coming i+=1
        elif op == "acc":
            acc += arg
        else:  # op == "nop"
            # Try switching it to a jump
            has_loop, final_acc = find_loop(instructions, visited, i + arg, acc)
            
            # If that eliminates cycle, return final acc value
            if not has_loop:
                return final_acc
        i += 1 

    # No loop found
    return -1

if __name__ == "__main__":

    # Parse input
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    # Execute instructions
    print("Accumulator contains {0} at the end".format(execute(lines)))
