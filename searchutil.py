import sys
import string

ESCAPES = ('\n', '\r', '\t', '\a')
WHITESPACE = ('\t', '\n', '\x0b', '\x0c', '\r', ' ')
LOWERCASE = tuple([i for i in string.lowercase])
UPPERCASE = tuple([j for j in string.uppercase])
ALPHABET = tuple([k for k in string.letters])
DIGITS = tuple([l for l in string.digits])
EXITWORDS = ('quit', 'exit', 'abort', 'done', 'end')

if "2." in sys.version[0:2]:
    _input = input
    def input(message=''):
        return raw_input(message)
    
def contains(needle, haystack):
    '''Checks for presence of each element of needle in haystack
    unless needle is a string then checks for needle in haystack'''
    if isinstance(needle, str):
        return needle in haystack
    return str_contains(needle, haystack)

def str_contains(needle, haystack):
    '''Checks for presence of each element of needle in haystack
    breaking strings into characters if necessary'''
    for i in needle:
        if i in haystack:
            return True
    return False


def findWithOverlap(phrase, haystack):
    '''A function that finds a phrase of characters
    of arbitrary length within a string. Returns
    a list of indexes of possibly overlapping occurrences the begin with the first char of the
    needle. '''
    phrase_list = []
    phrase_len = len(phrase)
    found = 0
    for i in range(0, len(haystack) - phrase_len, 1): # That '1' was the fatal mistake I needed to fix
        if phrase == haystack[i:i+phrase_len]:
            phrase_list.append(i)
    r = phrase_list if phrase_list else -1
    return r

def find(phrase, haystack):
    '''A function that finds a phrase of characters
    of arbitrary length within a string. Returns
    a list of indexes of non overlapping occurrences the begin with the first char of the
    needle. '''
    phrase_list = []
    phrase_len = len(phrase)
    found = 0
    for i in range(0, len(haystack) - phrase_len + 1, 1): # That '1' was the fatal mistake I needed to fix
        if found >= len(phrase):
            found = 0
        if found > 0 and found < len(phrase):
            found += 1
            continue
        if phrase == haystack[i:i+phrase_len]:
            phrase_list.append(i)
            found = 1
    r = phrase_list if phrase_list else -1
    return r

def isInvalidInt (x):
    '''Determine if x is a valid integer'''
    if not isinstance(x, str) and isinstance(x, int):
        return False
    if not isinstance(x, str) and not isinstance(x, int):
        return True
    if "." in x :
        return True
    for i in x:
        if i not in DIGITS:
            return True
    try:
        x = int(x)
        return False
    except Exception:
        return True
    return False

def rescanForInt (y):
    '''Continuously ask for input while y is not a valid int'''
    while isInvalidInt(y) :
        print "Sorry " + y + " is not a valid integer, please enter an integer"
        print "\nEnter a number: "
        y = input()
        if y in EXITWORDS:
            raise SystemExit
    return y

if __name__ == '__main__':
    print find('sss', 'ssssss')