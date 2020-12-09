# Day 9 Part 2

from part1 import find_invalid
from typing import List

def find_range(nums: List[int], target: int) -> int:
    """ Finds contiguous range that sums to given number."""
    i, j = 0, 1
    curr_sum = nums[i] + nums[j]

    while i < j and j < len(nums):
        # If current window sums to target, find sum of min and max
        if curr_sum == target:
            return min(nums[i:j + 1]) + max(nums[i:j + 1])
        # If current sum is too small, increase to the right
        elif curr_sum < target:
            j += 1
            curr_sum += nums[j]
        else:  # curr_sum > target:
            # If i and j are next to each other, we need to move 
            # both i and j to the right
            if i == j - 1:
                j += 1
                curr_sum += nums[j]
            # Or else, just move i to the right
            curr_sum -= nums[i]
            i += 1
   
    # No contiguous subarray found that sums to target
    return -1


if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        nums = [int(num) for num in file]

    # Define preamble size
    preamble = 25

    # Find invalid number to use as target
    target = find_invalid(nums, preamble)

    # Find sum of smallest and largest numbers in contiguous
    # range summing to first invalid number lol
    print("The sum of the first and last numbers of the\
        contiguous range is {0}".format(find_range(nums, target)))
