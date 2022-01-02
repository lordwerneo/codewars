"""
https://www.codewars.com/kata/52774a314c2333f0a7000688

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore,
the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):
    print(string)
    validation = 0
    for char in string:
        if validation < 0:
            return False
        if char == '(':
            validation += 1
        elif char == ')':
            validation -= 1
    return True if validation == 0 else False


print(valid_parentheses("((())()())"))
