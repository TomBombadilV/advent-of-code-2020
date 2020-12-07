# Day 7 Part 1

from collections import defaultdict
import re
from typing import Dict, List

def dfs_util(graph: Dict[str, List[str]], source: str, visited: Dict[str, bool]) -> None:
    # Visit all bags that contain source bag
    for bag in graph[source]:
        if not visited[bag]:
            visited[bag] = True
            dfs_util(graph, bag, visited)

def dfs(graph: Dict[str, List[str]], bag: str) -> int:
    """ Performs DFS from desired bag to find all bags 
        that can contain that bag.
    """
    # Make sure bag color exists    
    if bag not in graph:
        return -1

    # Keep track of visited nodes to avoid cycles
    visited = defaultdict(bool)
    for key in graph:
        visited[key] = False

    # Perform DFS from target bag
    visited[bag] = True
    dfs_util(graph, bag, visited)

    # Sum all true values in visited dictionary. All visited
    # bags can contain target bag
    res = 0
    for key in visited:
        if visited[key]:
            res += 1

    # Ignore shiny gold bag
    return res - 1

def build_graph(lines: List[str]) -> Dict[str, List[str]]:
    """ Takes lines of bag rules, builds a REVERSED graph 
        (a bag points to the bags that directly contain it)
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
            m = re.match("\s\d+\s([\w|\s]+)\sbags?", inner)
            if m:
                # Get matching group which is color name, add to dictionary
                inner_bag = m.group(1)
                dic[inner_bag].append(outer)
            # Should only be no match if it says "no other bags"
            else:
                #print("No match")
                pass
    
    return dic

def count_bags(rules: List[str], bag: str) -> int:
    """ Builds graph out of bag rules, then returns number
        of bags that can contain that bag
    """
    # Parse rules and build graph
    graph = build_graph(rules)

    # Perform DFS on graph starting from target bag
    return dfs(graph, bag)

if __name__ == "__main__":
    # Parse input
    with open("input_test.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Define target bag
    bag = "shiny gold"

    # Count bags that can contain given bag
    print("{0} bags can contain a {1} bag".format(count_bags(lines, bag), bag))
