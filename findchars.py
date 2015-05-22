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
