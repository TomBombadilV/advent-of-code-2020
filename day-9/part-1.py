# Day 9 Part 1

from typing import List, Set

def summable(n: int, preamble: Set[int]) -> bool:
    """ Takes a set of numbers and determines whether
        the target number is the sum of two numbers in 
        the set.
    """
    # Iterate through all values in set. If its "complement"
    # also exists in the set, then the target number is 
    # the sum of two numbers in the set.
    for addend in preamble:
        if n - addend in preamble:
            return True

    return False

def find_invalid(nums: List[int], n: int) -> int:
    """ Takes a list of numbers and a preamble length.
        Finds the first number in the list that is not the sum
        of any two numbers in the previous n numbers.
    """
    # If length of list is not greater than preamble size return -1
    if len(nums) <= n:
        return -1

    # Since we can assume the numbers are different, we can use set
    # Fill preamble set with first n numbers
    preamble = set(nums[:n])

    for i in range(n, len(nums)):
        # Check if number is a sum of two numbers in the preamble
        if not summable(nums[i], preamble):
            return nums[i]
        # If it is, then remove first number from preamble
        # and replace with current number, then continue
        else:
            preamble.remove(nums[i - n])
            preamble.add(nums[i])

    # No invalid number found
    return -1
    
if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        nums = [int(num) for num in file]

    # Define preamble length
    preamble = 25
    
    # Find first invalid number
    print("The first invalid number is", find_invalid(nums, preamble))
