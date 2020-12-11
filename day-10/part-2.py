# Day 10 Part 2

from typing import List

def count_ways(adapters: List[int]) -> int:
    """ Takes a list of adapter voltages, then counts
        the number of different valid combinations
        can be "chained" from outlet to device.
    """
    # Sort it
    adapters = sorted(adapters)
   
    # Add the outlet to the list of adapters
    adapters.insert(0, 0)

    # We need to calculate all adapters and the outlet to the adapters
    dp = [0 for _ in range(len(adapters))]
    
    # There is only one way for last adapter to reach outlet
    dp[-1] = 1

    # We need to calculate outlet and adapters 0...n - 1 (since
    # we already calculated the last adapter)
    for i in reversed(range(len(adapters) - 1)):
        # Look forward to find adapters in range
        j = i + 1
        while j < len(adapters) and adapters[j] - adapters[i] <= 3:
            # If adapter in range, add number of ways from that adapter
            dp[i] += dp[j]
            j += 1

    return dp[0]

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        adapters = [int(line) for line in file]

    # Calculate number of different ways
    print("There are {0} ways the adapters can be arranged".\
        format(count_ways(adapters)))
