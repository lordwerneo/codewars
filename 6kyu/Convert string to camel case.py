"""
https://www.codewars.com/kata/517abf86da9663f1d2000003

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case,
also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""
from time import time


def to_camel_case(text):
    result, upper = [], 0
    for char in text:
        if upper:
            result.append(char.upper())
            upper = 0
            continue
        if not char.isalpha():
            upper = 1
            continue
        result.append(char)
    return ''.join(result)


def to_camel_case_one(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


def to_camel_case_two(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])


start = time()
for _ in range(100000):
    to_camel_case('')
    to_camel_case("the_stealth_warrior")
    to_camel_case("The-Stealth-Warrior")
    to_camel_case("A-B-C")
print(time()-start)

start = time()
for _ in range(100000):
    to_camel_case_one('')
    to_camel_case_one("the_stealth_warrior")
    to_camel_case_one("The-Stealth-Warrior")
    to_camel_case_one("A-B-C")
print(time()-start)

start = time()
for _ in range(100000):
    to_camel_case_two('')
    to_camel_case_two("the_stealth_warrior")
    to_camel_case_two("The-Stealth-Warrior")
    to_camel_case_two("A-B-C")
print(time()-start)