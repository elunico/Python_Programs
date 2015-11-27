import math
import sys


QUITWORDS = ('quit', 'exit', 'done', 'kill', 'end')


if "2." in sys.version[:2]:
    _input = input
    input = raw_input


def is_prime(n):
    if n < 0:
        n = -n
    if n == 1 or n == 0:
        try:
            raise ValueError
        except ValueError:
            print("-1, 0, and 1 are neither prime nor non-prime")
            return None
    if n == 2:
        return True
    if n % 5 == 0 and n != 5:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def invalid(x):
    if '.' in x:
        return True
    try:
        x = int(x)
        return False
    except:
        return True
    return False


def redo(y):
    QUITWORDS = ('quit', 'exit', 'done', 'kill', 'end')
    while invalid(y):
        print("Sorry \"{0}\" is not a valid integer, please enter an integer".format(y))
        y = input("Enter a valid Number: ")
        if y in QUITWORDS:
            sys.exit()
    return int(y)


def main():
    x = input("Enter a Number: ")
    if x in QUITWORDS:
        sys.exit()
    x = redo(x)
    x = int(x)
    print(is_prime(x))


if __name__ == '__main__':
    while 1:
        main()
        print