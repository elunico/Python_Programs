# Created by Thomas

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.kind = ""
        self.health = 100
        self.money = 1000
        self.age = 18
        self.debt = 0
        self.credit = 700
        self.gender = ""
        self.employed = ""
        self.salary = 0
        self.happiness = 100
        self.isComplex = False

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def makeComplex(self):
        self.isComplex = True

    def getFired(self):
        if self.happiness < 40:
            self.salary = 200
            self.employed = ""
            self.happiness -= 25

    def getPropertyByName(self, element):
        return self.element

    def setPropertyByName(self, element, value):
        self.element = value

    def getJob(self, job, salary):
        self.employed = job
        self.salary = salary
        self.happiness -= 10

    def retire(self):
        self.salary = -12000
        self.employed = "Retiree"
        self.money -= self.debt
        self.health -= 10
        self.happiness += 25

    def getSalary(self):
        self.money += self.salary
        self.happiness += 2

    def isEmployed(self):
        if (self.employed):
            return True
        else:
            return False

    def inDebt(self):
        if self.debt:
            return True
        else:
            return False

    def canBorrow(self):
        if self.credit > 450 and self.kind == "human":
            return True
        else:
            return False

    def borrowMoney(self, amount):
        if self.credit < 450 or self.kind != "human":
            print("Cannot Borrow. Credit Rejected")
            return False
        limit = 2500
        if (self.credit > 670):
            limit = 5000
        if (amount <= limit):
            self.debt += amount
        else:
            print("You were denied your loan")

    def payLoan(self, amount):
        self.debt -= amount

    def interestGain(self):
        self.debt *= 1.045
        if (self.debt > 1000):
            self.credit -= 20
            self.grossSalary = self.salary
            self.salary -= 100
            self.salary = self.grossSalary
        elif (self.debt > 5000):
            self.credit -= 40
            self.grossSalary = self.salary
            self.salary -= 120
            self.salary = self.grossSalary
        elif (self.debt > 10000):
            self.credit -= 65
            self.grossSalary = self.salary
            self.salary -= 150
            self.salary = self.grossSalary
        elif ( not self.debt and self.credit < 796 ):
            self.credit += 5

    def setKind(self, kind):
        self.kind = kind

    def getKind(self):
        return self.kind

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def die(self, thing):
        print(thing.name + " has died.")

    def isAlive(self):
        if (self.health > 0):
            return True
        else:
            return False

    def agen(self):
        self.age+=1
        self.interestGain()
        self.getSalary()
        if (self.age == 18):
            print("\nGet out of my house!")
        if (self.age == 35):
            print("*Cries*")
            self.happiness -= 15
            self.getFired()
        if (self.age == 65):
            print("Retirement!")
            self.happiness += 10
            self.retire()
        if (self.age == 80):
            self.health = 0
            self.die(self)

        print("You are now " + str(self.age) + " years old")
        if (self.isEmployed()):
            print("You have a job as " + str(self.employed) + " and make " + str(self.salary))

        print("You have " + str(self.money) + " money.")
        print("Health: " + str(self.health) + "\n")
        if (not self.health):
            print("You are dead!\n")

    def hasName(self):
        if (self.name):
            return True
        else:
            return False

    def attack(self, thing):
        thing.health -= 10
        if (not thing.isAlive()):
            thing.die(thing)

    def removeComplex(self):
        self.isComplex = False


tom = Person("Tom", 68.5, 135)
nick = Person("Nick", 66.5, 129.4)
tom.setName("Tom")
nick.setName("Nick")
tom.setKind("human")
nick.setKind("human")
nick.health = 10
tom.attack(nick)
tom.getJob("Programmer", 230000)
nick.getJob("Actor", 1400000)
tom.borrowMoney(6500)
tom.agen()
tom.agen()
nick.agen()
nick.agen()
tom.payLoan(7000)
i = 0
while (i < 60):
    tom.agen()
    nick.agen()
    i+= 1
