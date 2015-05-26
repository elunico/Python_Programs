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
    def input(message):
        return raw_input(message)

def contains(haystack, needle):
	'''Checks for presence of each element of needle in haystack
	unless needle is a string then checks for needle in haystack'''
	if isinstance(needle, str):
		return needle in haystack
	str_contains(haystack, needle)

def str_contains(haystack, needle):
	'''Checks for presence of each element of needle in haystack
	breaking strings into characters if necessary'''
	for i in needle:
		if i in haystack:
			return True
	return False

def find(phrase, haystack):
    '''A function that finds a phrase of characters
    of arbitrary length within a string. Returns
    a list of indexes the begin with the first char of the
    needle. '''
    phrase_list = []
    phrase_len = len(phrase)
    for i in range(0, len(haystack) - phrase_len, 1): # That '1' was the fatal mistake I needed to fix
        if phrase == haystack[i:i+phrase_len]:
            phrase_list.append(i)
    r = phrase_list if phrase_list else -1
    return r

def isInvalidInt (x):
	'''Determine if x is a valid integer'''
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
	while invalid(y) :
		print "Sorry " + y + " is not a valid integer, please enter an integer"
		print "\nEnter a number: "
		y = input()
		if y in EXITWORDS:
			raise SystemExit
	return y
