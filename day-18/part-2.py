# Day 18 Part 1

from typing import List

def evaluate(expr: List[str], i: int) -> int:
    """ Evaluates mathematical expression """
    val = 0
    op = ""
    
    new_expr = []
    
    # Evaluate parentheses
    j = end_i = i
    while j < len(expr):
        if expr[j] == "(":
            res, j = evaluate(expr, j + 1)
            end_i = j
            new_expr.append(res)
        elif expr[j] == ")":
            
            break
        else:
            new_expr.append(expr[j])
        end_i += 1
        j += 1

    # Pivot to new expression list
    expr = new_expr
    new_expr = []

    # Evaluate addition
    i = 0
    while i < len(expr):
        if expr[i] == "+":
            new_expr[-1] = int(new_expr[-1]) + int(expr[i + 1])
            i += 1
        else:
            new_expr.append(expr[i])
        i += 1

    # Pivot to new expression list
    expr = new_expr
    
    # Evaluate multipliation
    res = 1
    i = 0
    while i < len(expr):
        if expr[i] != "*":
            res *= int(expr[i])
        i += 1

    return res, end_i

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
