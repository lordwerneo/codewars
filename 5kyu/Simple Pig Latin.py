"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    words = text.split()
    result = []
    for word in words:
        if word.isalpha():
            result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word)
    return ' '.join(result)


print(pig_it('Pig latin is cool'))
