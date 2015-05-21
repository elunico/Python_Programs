def find(phrase,haystack, phrase_len=1):
    '''A function that finds a phrase of characters
    of arbitrary length within a string. By default it will
    search for a phrase (needle) 1 character long'''
    phrase_list = []
    for i in range(0, len(haystack) - phrase_len, phrase_len):
        if phrase == haystack[i:i+phrase_len]:
            phrase_list.append(i)
    r = phrase_list if phrase_list else -1
    return r