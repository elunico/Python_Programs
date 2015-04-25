def find(ch,string1, charlen=1):
    pos = []
    for i in range(0, len(string1) - charlen, charlen):
        if ch == string1[i:i+charlen]:
            pos.append(i)
    r = pos if pos else -1
    return r