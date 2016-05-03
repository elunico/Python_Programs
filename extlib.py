# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import string
import re
import random
import imp

import tcolors


if "2." in sys.version[0:2]:
    VERSION = 2
    _input = input
    def input(message=''):
        return raw_input(message)
else:
    VERSION = 3
    xrange = range
    long = int


ESCAPES = ('\n', '\r', '\t', '\a')
WHITESPACE = tuple(n for n in string.whitespace)
LOWERCASE = tuple([i for i in string.lowercase]) if VERSION < 3 else tuple([i for i in string.ascii_lowercase])
UPPERCASE = tuple([j for j in string.uppercase]) if VERSION < 3 else tuple([j for j in string.ascii_uppercase])
ALPHABET = tuple([k for k in string.letters]) if VERSION < 3 else tuple([k for k in string.ascii_letters])
DIGITS = tuple([l for l in string.digits])
PUNCTUATION = tuple([m for m in string.punctuation])
EXITWORDS = ('quit', 'exit', 'abort', 'done', 'end')


def warn(msg, sep=' ', end='\n', file=sys.stdout):
    '''platform: darwin'''
    print(tcolors.warn + "WARNING: " + msg + tcolors.black, sep=sep, end=end, file=file)


def reverse(array):
    return list(reversed(array))


def pop_first(array):
    array.reverse()
    popd = array.pop()
    array.reverse()
    return popd


def contains(needle, haystack):
    return needle in haystack


def contains_any(list_of_items, iterable_haystack):
    '''iterates through the list of item and checks
    to see if ANY of the elements in the list are
    in the haystack using list_of_items[i] in
    iterable_haystack'''
    for i in list_of_items:
        if i in iterable_haystack:
            return True
    return False


def contains_all(list_of_items, iterable_haystack):
    for i in list_of_items:
        if i not in iterable_haystack:
            return False
    return True


def contains_only(list_of_items, iterable_haystack):
    for i in iterable_haystack:
        if i not in list_of_items:
            return False
    return True


def findWithOverlap(phrase, haystack):
    '''A function that finds a phrase of characters
    of arbitrary length within a string. Returns
    a list of indexes of possibly overlapping occurrences the begin with the first char of the
    needle. '''
    phrase_list = []
    phrase_len = len(phrase)
    for i in xrange(0, len(haystack) - phrase_len, 1): # That '1' was the fatal mistake I needed to fix
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
    for i in xrange(0, len(haystack) - phrase_len + 1, 1): # That '1' was the fatal mistake I needed to fix
        if found >= len(phrase):
            found = 0
        if found > 0 and found < len(phrase):
            found += 1
            continue
        if phrase == haystack[i:i+phrase_len]:
            phrase_list.append(i)
            found = 1
    r = phrase_list if phrase_list else []
    return r


def findWithRe(pattern, string, defaultValue=None):
    match = re.search(pattern, string)
    if not match:
        return defaultValue
    if match:
        return match.group()


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
        print("Sorry " + y + " is not a valid integer, please enter an integer")
        print("\nEnter a number: ")
        y = input()
        if y in EXITWORDS:
            raise SystemExit
    return y


def findandprint(needle, haystack, echo=True):
    temp = -1
    if contains(needle, haystack):
        q = find(needle, haystack)
        if echo:
            print("\n\nWe found {} occurrences of {} in {}\n".format(len(q), needle, haystack))
            for i in xrange(len(haystack)):
                if i in q:
                    print(tcolors.red, end = '')
                    temp = i + len(needle)
                if i == temp:
                    print(tcolors.end, end= '')
                print(haystack[i], end ='')
        else:
            return_string = ''
            for i in xrange(len(haystack)):
                if i in q:
                    return_string += tcolors.red
                    temp = i + len(needle)
                if i == temp:
                    return_string += tcolors.end
                return_string += haystack[i]
            return return_string
    else:
        print("\nNo matches found in {}".format(haystack))


def scan_for_bool(item):
    if isinstance(item, str):
        item = item.strip().lower()
        if item == "true":
            return 1
        if item == "false":
            return 0
    else:
        return bool(item)



def demo():
    a = input("Hello. Please enter any letters: ").lower().strip()
    b = "".join([LOWERCASE[random.randint(0, len(LOWERCASE)-1)] for i in xrange(400)])
    findandprint(a, b)
    print(); print()
    g = input("\n\nEnter an integer please: ")
    g = int(rescanForInt(g))
    print("\n\nThank you.")
    print("-*-*-*-*-*-*-*-*-*-END-*-*-*-*-*-*-*-*-*-")


if __name__ == '__main__':
    demo()
