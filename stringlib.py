# -*- coding: utf-8 -*-
import sys
import extlib


def usage():
    print ("Usage:\n$ python stringletters.py \"string\" [-cps ignore_all] "
           "[-c ignore_caps] [-s ignore_space] [-p ignore_punctuation]")
    raise SystemExit


def showChars(list_of_chars, string):
    lst = []
    for i in list_of_chars:
        if i in string:
            lst.append(string.index(i))
    return lst


def fixNonAscii(string):
    for i in string:
        if ord(i) > 127:
            string = string.replace(i, "")
    return string


def isAscii(string):
    """Checks to make sure all characters in <string>
    are ASCII returning true if so else false"""
    return all(ord(c) < 128 for c in string)


def findNonAscii(string):
    """Returns the index of the first non-ASCII
    character in <string> or -1 if string is
    ASCII"""
    nonasciis = []
    for c in string:
        if ord(c) >= 128:
            nonasciis.append(string.index(c) + 1)
    if not nonasciis:
        return -1
    else:
        return nonasciis


def parseArgs(arg_list):
    ic = ip = is_ = 0
    if (((not ('-c' in arg_list or '-s' in arg_list or
         '-p' in arg_list)) and (not ('-cps' in arg_list or
         '-pcs' in arg_list or '-psc' in arg_list or '-csp' in arg_list or
         '-scp' in arg_list or '-spc' in arg_list))) and len(arg_list) > 2):
        # THEN
        usage()
    try:
        if '-c' in arg_list:
            ic = extlib.scan_for_bool(arg_list[arg_list.index('-c') + 1])
        if '-p' in arg_list:
            ip = extlib.scan_for_bool(arg_list[arg_list.index('-p') + 1])
        if '-s' in arg_list:
            is_ = extlib.scan_for_bool(arg_list[arg_list.index('-s') + 1])
        # CURRENTLY NOT ALLOWED DUE TO USAGE CONSTRAINTS
        if '-cp' in arg_list:
            ic = ip = extlib.scan_for_bool(arg_list[arg_list.index('-cp') + 1])
        if '-cs' in arg_list:
            ic = is_ = extlib.scan_for_bool(arg_list[arg_list.index('-cs') + 1])
        if '-ps' in arg_list:
            is_ = ip = extlib.scan_for_bool(arg_list[arg_list.index('-ps') + 1])
        if '-pc' in arg_list:
            ic = ip = extlib.scan_for_bool(arg_list[arg_list.index('-pc') + 1])
        if '-sc' in arg_list:
            ic = is_ = extlib.scan_for_bool(arg_list[arg_list.index('-sc') + 1])
        if '-sp' in arg_list:
            is_ = ip = extlib.scan_for_bool(arg_list[arg_list.index('-sp') + 1])
        # END
        if '-cps' in arg_list:
            is_ = ip = ic = extlib.scan_for_bool(arg_list[arg_list.index('-cps') + 1])
        if '-csp' in arg_list:
            is_ = ip = ic = extlib.scan_for_bool(arg_list[arg_list.index('-csp') + 1])
        if '-spc' in arg_list:
            is_ = ip = ic = extlib.scan_for_bool(arg_list[arg_list.index('-spc') + 1])
        if '-scp' in arg_list:
            is_ = ip = ic = extlib.scan_for_bool(arg_list[arg_list.index('-scp') + 1])
        if '-psc' in arg_list:
            is_ = ip = ic = extlib.scan_for_bool(arg_list[arg_list.index('-psc') + 1])
        if '-pcs' in arg_list:
            is_ = ip = ic = extlib.scan_for_bool(arg_list[arg_list.index('-pcs') + 1])
        return (ic, ip, is_)
    except (IndexError, ValueError, TypeError):
        usage()


def isPangram(string, fix_non_ascii=False, strict=False):
    if strict:
        if not string.isalpha():
            raise ValueError("String is not alpha and strict mode is enabled")
    if not isAscii(string) and not fix_non_ascii:
        raise ValueError("Could not compare; remove the invalid chars: (use arg fix_non_ascii) ")
        print("Non ascii at {}".format(findnonAscii(string)))
        return False
    elif not isAscii(string) and fix_non_ascii:
        print("fixing non ascii...")
        string = fixNonAscii(string)
    string = string.lower().strip()
    for i in extlib.LOWERCASE:
        if i not in string:
            return False
    return True


def isPalindrome(string, ignore_caps=False, ignore_punc=False,
                 ignore_space=False, fix_non_ascii=False, 
                 strict=False):
    if strict:
        if not string.isalpha():
            raise ValueError("String is not alpha and strict mode is enabled")
    if not isAscii(string) and not fix_non_ascii:
        raise ValueError("Could not compare; remove the invalid chars: (use arg fix_non_ascii) ")
        print("Non ascii at {}".format(findnonAscii(string)))
        return False
    elif not isAscii(string) and fix_non_ascii:
        print("Fixing non ascii...")
        string = fixNonAscii(string)
    if ignore_caps:
        string = string.lower()
    if ignore_punc:
        for i in extlib.PUNCTUATION:
            string = string.replace(i, "")
    if ignore_space:
        for i in extlib.WHITESPACE:
            string = string.replace(i, "")
    if string[::-1] == string:
        return True
    return False


def main(argc, argv):
    ic, ip, is_ = parseArgs(argv)
    try:
        argv[1]
    except IndexError:
        usage()
    print(isPalindrome(argv[1], ic, ip, is_))


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
