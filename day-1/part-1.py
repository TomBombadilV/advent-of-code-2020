# Day 1: Report Repair

from typing import List

def findPair(nums: List, target: int) -> int:
    """ Finds pair of numbers in list that sum
        to given target, then returns their product
    """
    # Keep track of numbers encountered
    s = set()

    for n in nums:
        # If number's "complement" already encountered, pair found
        if target - n in s:
            print("Pair is {0} and {1}".format(target - n, n))
            return n * (target - n)
        # Else add to set
        else:
            s.add(n)
    return -1

def main():
    # Parse input file
    with open('input.txt', 'r') as file:
        nums = [int(line.strip()) for line in file]
   
    # Goal sum
    target = 2020

    # Find pair
    print("Product is {0}".format(findPair(nums, target)))

main()
