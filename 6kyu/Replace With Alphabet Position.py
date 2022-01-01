"""
https://www.codewars.com/kata/546f922b54af40e1e90001da

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""
from string import ascii_lowercase


def alphabet_position(text):
    position = dict(zip(ascii_lowercase, range(1, 27)))
    return ' '.join([str(position[x.lower()]) for x in text if x.isalpha()])
