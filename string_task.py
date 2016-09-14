# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#
# Example input: 'read'
# Example output: 'reading'
def verbing(s):
    if len(s) >= 3 and  s[-3:] == 'ing':
        answ = s[:-3] + 'ly'
    elif len(s) < 3:
        answ = s
    else:
        answ = s + 'ing'
    return answ


# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
#
# Example input: 'This dinner is not that bad!'
# Example output: 'This dinner is good!'
def not_bad(s):
    if s.find('not',0,-1) < s.find('bad',0,-1):
        answ = s[:s.find('not',0,-1)] +  'good' + s[s.find('bad',0,-1) + 3:]
    else:
        answ = s
    return answ


# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
#
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
#
# Example input: 'abcd', 'xy'
# Example output: 'abxcdy'
def front_back(a, b):
    afront = a[:(len(a) - len(a)//2)]
    bfront = b[:(len(b) - len(b)//2)]
    aback = a[(len(a) - len(a)//2):]
    bback = b[(len(b) - len(b)//2):]
    return afront + bfront + aback + bback
