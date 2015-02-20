import random

class Critter(object):
    total = 0
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredem = 0
        self._mood = self.hunger + self.boredem
        self.firstWords = False

    def __str__(self):
        return "Creature Object\nname: {0}\nboredom: {1}\nhunger: {2}".format(self.name, self.boredem, self.hunger)

    def getHungry(self):
        self.hunger += 10

    def getBored(self):
        self.boredem += 7

    @property
    def mood(self):
        self._mood = self.hunger + self.boredem
        if self._mood < 5:
            m = "happy"
        elif self._mood > 5 and self._mood < 12:
            m = "annoyed"
        elif self._mood > 12:
            m = "ANGRY!"
        return m

    def talk(self):
        greetings = ("Hello, how are you", "Can you talk too?",
                     "What's going on?", "*laugh*", "Now What? ")
        if not self.firstWords:
            return "Hello. I am {0}. Nice to meet you.".format(self.name)
            self.firstWords = True
        else:
            return random.choice(greetings)

    def feed(self, amount):
        self.hunger -= amount
        return "Thanks for the food. Yum..."

    def play(self, time):
        _time = time / (1.618 ** 2)
        self.boredem -= int(_time)
        return "That was fun!"

critters = {"crit1":Critter("Bob"), "crit2":Critter("Jimmy"), "crit3":Critter("Emily")}

critters["crit1"].getHungry()
critters["crit2"].getHungry()
critters["crit3"].getBored()
critters["crit1"].getHungry()
critters["crit2"].getBored()
critters["crit3"].getBored()
critters["crit3"].getHungry()
critters["crit2"].getBored()

for (key, value) in critters.items():
    print critters[key].talk()
    print critters[key].feed(2)
    print critters[key].play(10)
    print critters[key].mood
    print