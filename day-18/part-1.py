# Day 18 Part 1

from typing import List

def evaluate(expr: List[str], i: int) -> int:
    """ Evaluates mathematical expression """
    val = 0
    op = ""
    while i < len(expr):
        if expr[i] == "(":
            if op == "*":
                res, i = evaluate(expr, i + 1)
                val *= res       
            elif op == "+":
                res, i = evaluate(expr, i + 1)
                val += res
            elif op == "":
                val, i = evaluate(expr, i + 1)
            else:
                print("Invalid operator")
        elif expr[i] == ")":
            return val, i 
        elif expr[i] == "*":
            op = "*"
        elif expr[i] == "+":
            op = "+"
        else:
            if op == "*":
                val *= int(expr[i])
            elif op == "+":
                val += int(expr[i])
            elif op == "":
                val = int(expr[i])
            else:
                print("Invalid operator")
            op = ""
        i += 1          
    return val, i

def sum_eval(lines: List[str]) -> int:
    """ Evaluates all mathematical expressions, then sums them """
    res = 0
    for line in lines:
        val, _ = evaluate(list(line), 0)
        res += val
    
    return res

if __name__ == "__main__":
    # Parse input
    with open("input.txt", "r") as file:
        lines = [line.strip().replace(" ", "") for line in file]

    # Sum of all evaluated expressions
    print("The sum of all evaluated expressions is", sum_eval(lines))
