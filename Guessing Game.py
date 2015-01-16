import random

class Application:
	def __init__(self):
		self.h = 'h'; self.l = 'l'; self.yes = 'yes'
		self.answer = 'no'
		self.firstturn = True
		self.turns = 0
		self.exception = True

		self.lownumbers = [0]
		self.highnumbers =[0]
	def instructions(self):
		print("""I\'m going to guess your number
		start by entering the low end and high end of your number
		separated by a space in the next prompt

		As you respond to my guesses,
		\ttype an [l] if your number is lower than my guess
		\ttype an [h] if your number is higher
		\ttype [yes] if I guessed correctly

		I WILL NOT GUESS THE ENDPOINTS YOU ENTER BELOW!""")
		self.getRange()
	def getRange(self):
		while self.exception:
			self.liss = (input("\nEnter the low and high range of your number: ")).split()
			try:
				self.e = [int(e) for e in self.liss]
				self.exception = False
			except:
				print("Please use integers!")
				self.exception = True
		self.lownumbers[0] = self.e[0]
		self.highnumbers[0] = self.e[1]
	def main(self):
		self.instructions()
		while self.answer != 'yes' :
			if self.firstturn:
				self.guess = random.randint(self.lownumbers[-1], self.highnumbers[0])
				self.firstturn = False
			else:
				self.guess = random.randint(self.lownumbers[-1]+1, self.highnumbers[0]-1)
			self.answer = input( "\n\nIs {} your number? ".format(self.guess) )
			if self.answer == 'h' :
				self.lownumbers.append(self.guess)
				self.lownumbers = sorted(self.lownumbers)
			elif self.answer == 'l':
				self.highnumbers.append(self.guess)
				self.highnumbers = sorted(self.highnumbers)
			elif self.answer == 'yes':
				print("Gotcha!")
				print("Yay, I win and in only {} turns".format(self.turns))
			self.turns += 1
			if self.turns == 20:
				break
				print("Sorry, I couldn't get it")

def main():
	a = Application()
	a.main()
	
if __name__ == '__main__':
	main()