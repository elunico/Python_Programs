def find(phrase,haystack, phrase_len=1):
    '''A function that finds a phrase of characters
    of arbitrary length within a string. By default it will
    search for a phrase (needle) 1 character long. Returns
    a list of indexes the begin with the first char of the
    needle. '''
    phrase_list = []
    for i in range(0, len(haystack) - phrase_len, 1): # That '1' was the fatal mistake I needed to fix
        if phrase == haystack[i:i+phrase_len]:
            phrase_list.append(i)
    r = phrase_list if phrase_list else -1
    return r
