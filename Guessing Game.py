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
		print("\nI\'m going to guess your number\n"
		"start by entering the low end and high end of your number\n"
		"separated by a space in the next prompt\n\n"

		"As you respond to my guesses,\n"
		"\ttype an [l] if your number is lower than my guess\n"
		"\ttype an [h] if your number is higher\n"
		"\ttype [yes] if I guessed correctly\n\n"

		"I WILL NOT GUESS THE ENDPOINTS YOU ENTER BELOW!")
		self.getRange()
	def getRange(self):
		while self.exception:
			try:
				self.liss = (raw_input("\nEnter the low and high range of your number: ")).split()
				self.e = [int(e) for e in self.liss]
				self.exception = False
			except:
				print("Please enter the LOW and HIGH range of your number--use integers!")
				self.exception = True
		self.lownumbers[0] = self.e[0]
		self.highnumbers[0] = self.e[1]
	def main(self):
		self.instructions()
		while self.answer != 'yes' :
			self.turns += 1
			try:
				if self.firstturn:
					self.guess = random.randint(self.lownumbers[-1], self.highnumbers[0])
					self.firstturn = False
				else:
					self.guess = random.randint(self.lownumbers[-1]+1, self.highnumbers[0]-1)
			except ValueError:
				print("Hmmm.... that's odd, there are no integers greater than {0} and less than {1}"\
				"\nPerhaps you have made a mistake.".format(self.lownumbers[-1], self.highnumbers[0]))
				raise SystemExit(3)
			self.answer = raw_input( "\n\nIs {} your number? ".format(self.guess) )
			while self.answer != "h" and self.answer != 'l' and self.answer != 'yes':
				self.answer = raw_input( "\n\nIs your number [h]igher or [l]ower than {0}; \nor is {0} your number [yes]? ".format(self.guess) )
			if self.answer == 'h' :
				self.lownumbers.append(self.guess)
				self.lownumbers = sorted(self.lownumbers)
			elif self.answer == 'l':
				self.highnumbers.append(self.guess)
				self.highnumbers = sorted(self.highnumbers)
			elif self.answer == 'yes':
				print("Got it")
				print("I win and in only {} turns".format(self.turns))
				return 0
			if self.turns == 25:
				print("Sorry, I couldn't get it!\nYOU WIN!")
				break


def main():
	a = Application()
	a.main()

if __name__ == '__main__':
	main()