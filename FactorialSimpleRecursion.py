import sys

def fac(x):
	if x <= 1:
		return 1
	elif x > 1:
		return x * fac(x-1)

def main():
	if len(sys.argv) < 2:
		print("Usage: Input a number to factorial as the second argument")
		raise SystemExit("Insufficient Number of Arguments")
	if '.' in sys.argv[1]:
		try:
			raise ValueError
		except ValueError:
			print("ValueError: Can only take the factorial of integers with this program\n")
			raise SystemExit(1)
	else:
		try:
			sys.argv[1] = int(sys.argv[1])
		except:
			print("Sorry You have to pass an integer.")
	x = str( fac(sys.argv[1] ) )
	print( "\n" + x + "\n" )

if __name__ == '__main__':
    main()

