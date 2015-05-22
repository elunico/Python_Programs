# Ported from Ruby
import math
EXITWORDS = ['quit', 'exit', 'abort', 'done', 'end']
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
def invalid (x):
  if "." in x :
    return True
  for i in x:
      if i not in NUMBERS:
        return True
  try:
    x = int(x)
  except Exception:
    return True
  return False

def redoer (y):
  while invalid(y) :
    print "Sorry " + y + " is not a valid integer, please enter an integer"
    print "\nEnter a number: "
    y = raw_input()
    if y in EXITWORDS:
      raise SystemExit
  return y

def factor(n):
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

def main():
  print "Enter an integer or \"quit\" to quit"
  num = raw_input()
  if num in EXITWORDS :
    raise SystemExit
  num = redoer(num)
  num=int(num)
  fs, nfs = factor(num)
  for i in fs:
      print(i)
  for i in nfs:
      print(i)
  print("")

if __name__ == '__main__':
    while 1:
      main()
