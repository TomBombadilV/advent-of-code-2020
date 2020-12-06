# Day 1 Part 2

from typing import List

def findTriple(nums: List, target: int) -> int:
    """ Finds triple of numbers that sum to given target,
        then returns their product.
    """

    # Sort list
    nums = sorted(nums)

    # Iterate through list where n is first number of triple 
    for i, n in enumerate(nums):

        # If n is larger than target, can't create target
        if n >= target:
            break

        # Use two pointers to attempt to locate desired pair in right window
        left, right = i + 1, len(nums) - 1
        while left < right: 
            currSum = n + nums[left] + nums[right]
            
            if currSum < target:    
                left += 1
            elif currSum > target:
                right -= 1
            else:
                print("Triple is {0}, {1}, and {2}".format(n, nums[left], nums[right]))
                return n * nums[left] * nums[right]

    return -1

def main():

    # Parse input file
    with open('input.txt', 'r') as file:
        nums = [int(line.strip()) for line in file]

    # Goal sum
    target = 2020

    # Find triple
    print("Product: {0}".format(findTriple(nums, target)))

main()
