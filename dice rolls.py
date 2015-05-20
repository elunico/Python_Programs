# Thomas Povinelli
# branching.py
# May 18-19, 2015
# 105 minutes
# 2 languages - 1 living; 1 dead
# 64000 successful tests in less than 7 seconds

'''
I wrote this for a game. It involved a long and complex
flow chart of possibilities that had to be individually
tested by dice rolling and keeping track.

I digitized the dice rolling and looping flow chart
using recursion and random numbers so rather than
follow an ungodly sum of dice rolls and a tiny flow chart
one simply has to run this program to decide if they
strike ore or not or if they die and they lose.

Unless of course you like rolling dice, in which case
I encourage you to endulge your passions.
'''

from __future__ import print_function
import random
import time
import sys

# Python 2 catch
if '2.' in sys.version[0:2]:
    def input(message):
        return raw_input(message)

# Global count weeks
# each call to a function is a week of time in the game
global WEEKS
WEEKS = 0

class bcolors:
    '''Constants used to change terminal color'''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printf(string):
    '''Optionally delayed printing for dramatic effect'''
    print(string)
    if '-s' in sys.argv:
        time.sleep(1.3)

def roll() :
    '''Two six sided dice are rolled'''
    r = random.randint(2, 13)
    return r;

# Keeps track of player's traits during the proceedings of the chart
class person_t(object):
    '''Person object that keeps track of special traits'''
    def __init__(self):
        self.admin = 1; self.bribery = 1; self.leader = 1; self.carousing = 1; self.eng = 1; self.ship_boat = 1; self.prosp = 1; self.vacc_suit = 1; self.nav = 1;

    
# Begin Flow Chart
    
def prospect1(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Prospecting...")
    a = roll() + p.prosp + p.eng + p.vacc_suit
    if a <= 5:
        result = moveToTrojan(p)
    elif a >= 6 and a <= 8:
        result = prospect2(p)
    else:
        result = restAndRec(p)
    return result

def prospect2(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Prospecting...")
    a = roll() + p.prosp + p.eng + p.vacc_suit
    if a <= 8:
        result = prospect1(p)
    elif a >= 9 and a <= 11:
        result = danger(p)
    else:
        result = 3
    return result

def moveToTrojan(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Prospecting...")
    a = roll()
    if a <= 4:
        result = needRefuel(p)
    elif a >= 5 and a <= 6:
        result = selectAreaOfProspect(p)
    elif a >= 7 and a <= 8:
        result = moveToBeltFringe(p)
    else:
        result = prospect1(p)
    return result

def moveToRRA(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Move to rumored area...")
    a = roll()
    if a <= 6:
        result = moveToCurrentProducingArea(p)
    elif a >= 7 and a <= 9:
        result = prospect1(p)
    elif a >= 10 and a <= 12:
        result = restAndRec(p)
    else:
        result = 3
    return result

def restAndRec(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Move to Rest and Recreation...")
    a = roll()
    if a < 5:
        result = moveToRRA(p)
    elif a >= 6 and a <= 10:
        result = prospect1(p)
    else:
        result = prospect2(p)
    return result

def moveToCurrentProducingArea(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Move to current producing area...")
    a = roll()
    if a >= 8:
        result = moveToRRA(p)
    elif a <= 7 and a >= 4:
        result = prospect1(p)
    else:
        result = selectAreaOfProspect(p)
    return result

def moveToBeltFringe(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Move to belt fringe...")
    a = roll()
    if a <= 4:
        result = refuel(p)
    elif a <= 5:
        result = moveToTrojan(p)
    elif a >= 6 and a <= 7:
        result = prospect2(p)
    else:
        result = prospect2(p)

def danger(p):
    global WEEKS 
    WEEKS += 1 
    printf(bcolors.FAIL + ">> Danger!" + bcolors.ENDC)
    a = roll()
    if a >= 6 and a <= 9:
        result = 2
    elif a <= 5:
        result = 4
    else:
        result = prospect2(p)
    return result

def refuel(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Refuel...")
    a = roll() + p.eng + p.ship_boat
    if a >= 8:
        result = moveToBeltFringe(p)
    else:
        result = danger(p)
    return result

def needRefuel(p):
    global WEEKS 
    WEEKS += 1 
    printf(">> Need Refuel...")
    a = roll()
    if a <= 10:
        result = refuel(p)
    else:
        result = 2
    return result

def patronAssists(p):
    global WEEKS 
    WEEKS += 1 
    printf(bcolors.OKGREEN + ">> Patron assists..." + bcolors.ENDC)
    a = roll() + p.leader
    if a >= 10:
        result = makeSpecialApplication(p)
    else:
        result = needRefuel(p)
    return result

def selectAreaOfProspect(p) :
    global WEEKS 
    WEEKS += 1 
    printf(">> Selecting Area of Prospect...")
    attempt = roll() + p.eng + p.nav;
    if (attempt <= 4) :
        result = moveToTrojan(p)
    elif (attempt >= 5 and attempt <= 8) :
        result = prospect1(p)
    else :
        result = moveToCurrentProducingArea(p)
    return result;

def goNoLicense(p) :
    global WEEKS 
    WEEKS += 1 
    printf(">> Go mine without license...")
    attempt = roll();
    if (attempt <= 5) :
        result = seekPatron(p);
    else :
        result = selectAreaOfProspect(p);
    return result;

def seekPatron (p) :
    global WEEKS 
    WEEKS += 1 
    printf(">> Seek patron...")
    attempt = roll();
    if (attempt <= 4) :
        result = applicationDenied(p);
    elif (attempt >= 5 and attempt >= 8) :
        result = patronAssists(p);
    else :
        result = goNoLicense(p);
    return result;

def makeSpecialApplication(p) :
    global WEEKS 
    WEEKS += 1 
    printf(">> Make Special Application...")
    attempt = roll();
    if (attempt>= 9 ) :
        printf(bcolors.OKGREEN + ">> License Granted!" + bcolors.ENDC)
        result = selectAreaOfProspect(p);
    else :
        result = applicationDenied(p);
    return result;

def considerBribe(p) :
    global WEEKS 
    WEEKS += 1 
    printf(">> Consider Bribery...")
    attempt = roll();
    if (attempt >= 8) :
        result = offerBribe(p);
    elif (attempt >=6 and attempt <=7) :
        result = makeSpecialApplication(p) ;
    else :
        result = applicationDenied(p);
    return result;

def offerBribe(p) :
    global WEEKS 
    WEEKS += 1 
    printf(">> Offer bribery...")
    attempt = roll();
    if (attempt <= 5) :
        result = considerBribe(p);
    elif (attempt >= 6 and attempt <= 9) :
        result = apply(p);
    else :
        printf(bcolors.OKGREEN + ">> License Granted!" + bcolors.ENDC)
        result = selectAreaOfProspect(p);
    return result;

def apply(p) :
    global WEEKS 
    WEEKS += 1 
    printf(bcolors.OKGREEN + ">> Begin Application..." + bcolors.ENDC)
    apply = roll();
    if (apply <= 7) :
        result = applicationDenied(p);
    else :
        result = offerBribe(p);
    return result;

def applicationDenied(p) :
    global WEEKS 
    WEEKS += 1 
    printf(">> Application Denied...")
    attempt = roll();
    if (attempt <= 3) :
        result = apply(p);
    elif (attempt >= 4 and attempt <= 6) :
        result = offerBribe(p);
    elif (attempt == 7) :
        result = makeSpecialApplication(p);
    elif (attempt == 8 or attempt == 9) :
        result = seekPatron(p);
    else :
        result = goNoLicense(p);
    return result;

# End flow chart functions
# Begin number functions
def invalid(x):
    '''Determine if x is an integer
    against several tests'''
    if '.' in x:
        return True
    try:
        x = int(x)
        return False
    except:
        return True
    return False

def redo(y):
    '''Require input from the user as long as
    the input is not a valid integer or \'quit\''''
    QUITWORDS = ('quit', 'exit', 'done', 'kill', 'end')
    while invalid(y):
        print("Sorry \"{0}\" is not a valid integer, please enter an integer".format(y))
        y = input("Enter a valid Number or (S to specify): ")
        if y in QUITWORDS:
            sys.exit()
    return int(y)

# End number functions
# Maintainence functions
def assign():
    p = person_t()
    x = int(input("Enter Skill for Enginerring: "))
    y = int(input("Enter Skill for Admin: "))
    z = int(input("Enter Skill for Bribery: "))
    a = int(input("Enter Skill for Leader: "))
    b = int(input("Enter Skill for Carousing: "))
    c = int(input("Enter Skill for Ship_Boat: "))
    d = int(input("Enter Skill for Prosperity: "))
    e = int(input("Enter Skill for Vac Suit: "))
    f = int(input("Enter Skill for navigation: "))
    p.eng = x; p.admin = y; p.bribery = z; p.leader = a; p.carousing = b; p.ship_boat = c; p.prosp = d; p.vacc_suit = e; p.nav = f;
    return p

def getStrikeRoll():
    a = random.randint(1, 10)
    b = random.randint(1, 8)
    c = "0" * b
    d = str(a) + c
    return int(d)

# End maintenance function

def main () :
    global WEEKS 
    x = input("Put in a number for all skills and hit enter \nOr type (S) and enter to specify each trait\nEntering nothing defaults all to 1: ")
    if not x:
        p = person_t()
    elif x.strip() in ('s', 'S'):
        p = assign()
    else:
        p = person_t()
        x = redo(x)
        p.admin =  p.bribery =  p.leader =  p.carousing =  p.eng =  p.ship_boat =  p.prosp =  p.vacc_suit =  p.nav = x;
    printf(bcolors.OKBLUE + "\n\nYou apply for a license" + bcolors.ENDC)
    result = apply(p);
    if (result == 1) :
        printf("Belting")
        printf(bcolors.OKBLUE + "Total weeks: " + str(WEEKS) + bcolors.ENDC)
        return result
    elif result == 2:
        printf(bcolors.FAIL + "Dead"+ bcolors.ENDC)
        printf(bcolors.OKBLUE + "Total weeks: " + str(WEEKS) + bcolors.ENDC)
        return result
    elif result == 3:
        printf(bcolors.OKGREEN + "Strike: " + str(getStrikeRoll()) + bcolors.ENDC)
        printf(bcolors.OKBLUE + "Total weeks: " + str(WEEKS) + bcolors.ENDC)
        return result
    printf("End")
    printf(bcolors.OKBLUE + "Total weeks: " + str(WEEKS) + bcolors.ENDC)
    return 0;

# Usage function
def usage():
    '''Check if usage is appropriate'''
    if len(sys.argv) > 2 or ('-s' not in sys.argv and len(sys.argv) > 1):
        raise SystemExit("Usage: $ python \"dice rolls.py\" [-s]\n-s : proceed slowly\n")

# if-main
if __name__ == '__main__':
    usage()
    main()