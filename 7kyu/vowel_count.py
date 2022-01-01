"""
https://www.codewars.com/kata/54ff3102c1bad923760001f3

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum([sentence.count(letter) for letter in vowels])
