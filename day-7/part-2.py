# Day 7 Part 2

from collections import defaultdict
from typing import Dict, List

import re

def dfs_util(graph: Dict[str, List[str]], source: str) -> int:
    # Count of bags including outer bag
    bag_sum = 1
  
    # Base case! If bag doesn't contain other bags, count one bag
    if len(graph[source]) == 0:
        return bag_sum

    # Visit all bags that are contained by source bag
    for elem in graph[source]:
        bag, count = elem
        res = dfs_util(graph, bag)
        # If source bag countains n inner bags, multiply the number 
        # of bags contained by inner bag by n
        bag_sum += count * res

    # Sum should be all inner bags plus outer bag
    return bag_sum

def dfs(graph: Dict[str, List[str]], bag: str) -> int:
    """ Performs DFS from desired bag to find all bags 
        that can contain that bag.
    """
    # Make sure bag color exists    
    if bag not in graph:
        return -1

    # Perform DFS from target bag
    res = dfs_util(graph, bag)
    
    # Ignore first bag
    return res - 1

def build_graph(lines: List[str]) -> Dict[str, List[str]]:
    """ Takes lines of bag rules, builds a graph (a bag points 
        to the bags that it directly contains, and the number required)
    """
    # Dictionary representation of graph
    dic = defaultdict(list)
   
    # Parse each rule and add to dictionary
    for line in lines:

        # Remove period
        line = line[:-1]
        # Separate outer bag from inner bags
        outer, inners = line.split(" bags contain")
        # Create list of inner bags
        inners = inners.split(",")
        
        # Parse inner bag string using regex
        for inner in inners:
            # Should take the form " 123 red bags"
            m = re.match("\s(\d+)\s([\w|\s]+)\sbags?", inner)
            if m:
                # Get matching group which is color name, add to dictionary
                count, inner_bag = int(m.group(1)), m.group(2)
                dic[outer].append((inner_bag, count))
            # Should only be no match if it says "no other bags"
            else:
                #print("No match")
                pass
    
    return dic

def count_bags(rules: List[str], bag: str) -> int:
    """ Builds graph out of bag rules, then returns number
        of bags that must be contained by that bag
    """
    # Parse rules and build graph
    graph = build_graph(rules)

    # Perform DFS on graph starting from target bag
    return dfs(graph, bag)

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Define target bag
    bag = "shiny gold"

    # Count bags contained by target bag
    print("{0} bags are contain by a {1} bag".format(count_bags(lines, bag), bag))
