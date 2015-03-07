import math

class NUMCHK(object):
  NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  def invalid (self, x):
    if "." in x :
      return True
    for i in x:
        if i not in NUMCHK.NUMBERS:
          return True
    try:
      x = int(x)
    except Exception:
      return True
    return False

  def redoer (self, y):
    while self.invalid(y) :
      print "Sorry " + y + " is not a valid integer, please enter an integer"
      print "\nEnter a number: "
      y = raw_input()
    return y


class FACTORER(object):
  EXITWORDS = ['quit', 'exit', 'abort', 'done', 'end']
  def factor(self, n):
    factors = []
    newfactors = []
    if n < 0 :
      n = -n
    if n == 1 :
      return 1
    elif n == 2 :
      return 1, 2
    elif n == 0 :
      try:
        raise Exception
      except Exception:
        print "Please Enter a non-zero integer"
    i = 1
    while i < (int(math.sqrt(n)) + 1) :
      if n % i == 0 :
        factors.append(i)
      i+=1
    for j in reversed(factors):
      newfactors.append(n/j)
    return factors, newfactors

  def main(self):
    print "Enter an integer or \"quit\" to quit"
    num = raw_input()
    if num in FACTORER.EXITWORDS :
      raise SystemExit
    num = NUMCHK().redoer(num)
    num=int(num)
    fs, nfs = self.factor(num)
    for i in fs:
        print(i)
    for i in nfs:
        print(i)
    print("")


def main():
    while True:
        FACTORER().main()

if __name__ == '__main__':
    main()