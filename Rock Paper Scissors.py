try:
	from Tkinter import * #Python 2 catch
except ImportError:
	from tkinter import *

import random 

choices = ['rock', 'paper', 'scissors']
def quitWin(w):
	w.destroy()
	w.quit()

class Application(object):
	def win(self):
		self.move = Tk()
		self.move.title("Pick your move!")
		self.move.geometry("+100+100")
		scissors = Button(self.move, text="scissors", font=("Helvetica Neue", "18", "bold"), command= lambda: F.userScissors(self.move))
		rock = Button(self.move, text="rock", font=("Helvetica Neue", "18", "bold"), command=lambda: F.userRock(self.move))
		paper = Button(self.move, text="paper", font=("Helvetica Neue", "18", "bold"), command=lambda: F.userPaper(self.move))
		quiter = Button(self.move, text="quit", font=("Helvetica Neue", "18", "bold"), command=quit)
		scissors.pack(pady=7, padx=7, side=LEFT)
		rock.pack(pady=7, padx=7, side=LEFT)
		paper.pack(pady=7, padx=7, side=LEFT)
		quiter.pack(pady=7, padx=7, side=LEFT)
		self.move.mainloop()

class Functions(object):
	def __init__(self):
		self.sc = 0
		self.pp = 0
		self.rk = 0
		self.cscore = 0
		self.pscore = 0
		self.score = Tk()
		self.score.title("Score")
		self.score.geometry("+500+100")
		self.scoreC = Label(self.score, text=self.cscore)
		self.scoreP = Label(self.score, text=self.pscore)
		self.scoreLC = Label(self.score, text="CPU Score:")
		self.scoreLP = Label(self.score, text="Player Score:")
		self.scoreC.grid(row = 0, column =1)
		self.scoreP.grid(row = 1, column=1)
		self.scoreLC.grid(row=0, column=0)
		self.scoreLP.grid(row=1, column=0)
	def userScissors(self, jmove):
		self.userMove = 'scissors'
		self.cpuMove = random.choice(choices)
		if self.cpuMove == 'rock':
			F.lose(self.userMove, 'rock')
		elif self.cpuMove == 'scissors':
			F.draw(self.userMove)
		elif self.cpuMove == 'paper':
			F.win(self.userMove, 'paper')
		self.sc += 1
		jmove.destroy()
		jmove.quit()
	def userPaper(self, jmove):
		self.userMove = 'paper'
		self.cpuMove = random.choice(choices)
		if self.cpuMove == 'rock':
			F.win(self.userMove, 'rock')
		elif self.cpuMove == 'scissors':
			F.lose(self.userMove, 'rock')
		elif self.cpuMove == 'paper':
			F.draw(self.userMove)
		self.pp += 1
		jmove.destroy()
		jmove.quit()
	def userRock(self, jmove):
		self.userMove = 'rock'
		self.cpuMove = random.choice(choices)
		if self.cpuMove == 'rock':
			F.draw(self.userMove)
		elif self.cpuMove == 'scissors':
			F.win(self.userMove, 'scissor')
		elif self.cpuMove == 'paper':
			F.lose(self.userMove, 'paper')
		self.rk += 1
		jmove.destroy()
		jmove.quit()
	def lose(self, p, c):
		alert = Tk()
		alert.title("you lost!")
		alert.geometry("+100+100")
		Label(alert, text="You lost! You called {} and the Computer called {}".format(p, c), font=("Helvetica Neue", "18", "bold")).pack()
		Button(alert, text="Close", command = lambda: quitWin(alert), font=("Helvetica Neue", "18", "bold")).pack()
		self.cscore += 1
		self.scoreC = Label(self.score, text=self.cscore)
		self.scoreC.grid(row = 0, column =1)
		self.score.update()
		alert.mainloop()
	def win(self, p, c):
		alert = Tk()
		alert.title("you win!")
		alert.geometry("+100+100")
		Label(alert, text="You WON! You called {} and the Computer called {}".format(p, c), font=("Helvetica Neue", "18", "bold")).pack()
		Button(alert, text="Close", command = lambda: quitWin(alert), font=("Helvetica Neue", "18", "bold")).pack()
		self.pscore += 1
		self.scoreP = Label(self.score, text=self.pscore)
		self.scoreP.grid(row = 1, column=1)
		self.score.update()
		alert.mainloop()
	def draw(self, p):
		alert = Tk()
		alert.title("Tie!")
		alert.geometry("+100+100")
		Label(alert, text="You tied. You both called {}".format(p), font=("Helvetica Neue", "18", "bold")).pack()
		Button(alert, text="Close", command = lambda: quitWin(alert), font=("Helvetica Neue", "18", "bold")).pack()
		alert.mainloop()

A = Application()
F = Functions()
while 1:
	A.win()

