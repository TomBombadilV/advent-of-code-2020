# Day 19 Part 1

from typing import Dict, List, Set

def parse_rule(rules: Dict[str, str], key: str) -> Set[str]:
    """ Takes a dictionary of rules, takes one rule and makes
        all possible matches out of it into a set
    """
    if rules[key] == ['"a"']:
        return {"a"}
    if rules[key] == ['"b"']:
        return {"b"}

    # Keep track of all final messages
    messages = set()

    # For each subrule in a rule (ex: 1 3 | 3 1)
    for sub_rule in rules[key]:
        # Find all possible messages for this subrule
        rule_messages = ['']
        
        # Split the subrule into parts
        parts = sub_rule.split(" ")
        
        # Parse each part separately
        for part in parts:
            # Get list of all possible messages for that part
            res = parse_rule(rules, part)
            
            # Create combinations of every rule message so far
            # with every combination returned for current part
            rule_messages = [rule_message + r\
                for rule_message in rule_messages\
                for r in res]
        
        # Add messages generated by this subrule to the final 
        # message set
        messages = messages | set(rule_messages)
    return messages

def num_matches(rules: Dict[str, List[str]], messages: List[str], rule: str) -> int:
    """ Takes a dictionary of rules, a list of messages, and
        counts how many messages match the first rule
    """
    matches = 0
    
    # Calculate all possible messages
    possible_messages = parse_rule(rules, rule)

    # Check if each rule matches the indicated rule
    for message in messages:
        matches += message in possible_messages

    return matches

if __name__ == "__main__":
    # Save rules in dictionary
    rules = {}
    messages = []

    # Parse input
    with open("input.txt", "r") as file:
        # Get rules
        line = file.readline()
        while line != "\n":
            key, val = line.split(": ")
            val = val.split('|')
            val = [rule.strip() for rule in val]
            rules[key] = val
            line = file.readline()

        # Throw away newline
        line = file.readline()
    
        # Get messages
        while line:
            messages.append(line.strip())
            line = file.readline()

    print(rules)
    print(messages)

    # Define rule to be matched
    rule = '0'

    # Count number of messages that match indicated rule
    print("There are {0} messages that match rule {1}".\
        format(num_matches(rules, messages, rule), rule))
