#!/usr/bin/python
try:
	from Tkinter import * #Python 2 catch
except ImportError:
	from tkinter import * #Python 3 catch

import random

class Application(object):
	def window(self):
		self.userScissors()
	
	def computerMove(self):
		if self.result == 'draw':
			if self.last == 'rock':
				self.cpuMove = 'scissors'
			elif self.last == 'paper':
				self.cpuMove = 'rock'
			elif self.last == 'rock':
				self.cpuMove = 'paper'
		elif self.result == 'win':
			self.cpuMove = random.choice(self.choices)
		elif self.result == 'lose':
			if self.last == 'rock':
				self.cpuMove = 'scissors'
			elif self.last == 'scissors':
				self.cpuMove = 'paper'
			elif self.last == 'paper':
				self.cpuMove = 'rock'
		else:
			self.cpuMove = random.choice(self.choices)
		return self.cpuMove
	
	def computer2Move(self):
		if self.result2 == 'draw':
			if self.last == 'rock':
				self.cpuMove = 'scissors'
			elif self.last == 'paper':
				self.cpuMove = 'rock'
			elif self.last == 'rock':
				self.cpuMove = 'paper'
		elif self.result2 == 'win':
			self.cpuMove = random.choice(self.choices)
		elif self.result2 == 'lose':
			if self.last == 'rock':
				self.cpuMove = 'scissors'
			elif self.last == 'scissors':
				self.cpuMove = 'paper'
			elif self.last == 'paper':
				self.cpuMove = 'rock'
		else:
			self.cpuMove = random.choice(self.choices)
		return self.cpuMove
	
	def __init__(self):
		self.choices = ['rock', 'paper', 'scissors']
		self.last = ''
		self.result = ''
		self.result2 = ''
		self.sc = 0
		self.pp = 0
		self.rk = 0
		self.cscore = 0
		self.pscore = 0
		self.tscore = 0
		self.score = Tk()
		self.score.title("Score")
		self.score.geometry("+500+100")
		self.scoreC = Label(self.score, text=self.cscore)
		self.scoreP = Label(self.score, text=self.pscore)
		self.scoreT = Label(self.score, text=self.tscore)
		self.scoreLC = Label(self.score, text="CPU2 Score:")
		self.scoreLP = Label(self.score, text="CPU Score:")
		self.scoreLT = Label(self.score, text="Ties:")
		self.scoreC.grid(row = 0, column =1)
		self.scoreP.grid(row = 1, column=1)
		self.scoreLC.grid(row=0, column=0)
		self.scoreLP.grid(row=1, column=0)
		self.scoreLT.grid(row = 2, column =0)
		self.scoreT.grid(row=2, column=1)
		self.window()
	
	def userScissors(self):
		self.last = 'scissors'
		self.userMove = self.computerMove()
		self.cpuMove = self.computer2Move()
		if self.cpuMove == 'rock':
			self.lose(self.userMove, 'rock')
		elif self.cpuMove == 'scissors':
			self.draw(self.userMove)
		elif self.cpuMove == 'paper':
			self.win(self.userMove, 'paper')
		self.sc += 1
	
	def lose(self, p, c):
		self.result = 'draw'
		self.result2 = 'win'
		self.cscore += 1
		self.scoreC = Label(self.score, text=self.cscore)
		self.scoreC.grid(row = 0, column =1)
		self.score.update()
	
	def win(self, p, c):
		self.result = 'lose'
		self.result2 = 'win'
		self.pscore += 1
		self.scoreP = Label(self.score, text=self.pscore)
		self.scoreP.grid(row = 1, column=1)
		self.score.update()
	
	def draw(self, p):
		self.result = 'win'
		self.result2 = 'win'
		self.tscore += 1
		self.scoreT = Label(self.score, text=self.tscore)
		self.scoreT.grid(row=2, column=1)
		self.score.update()
	

def main():
	A = Application()
	for i in range(100):
		A.window()
	raw_input("_ ")

if __name__ == '__main__':
	main()
