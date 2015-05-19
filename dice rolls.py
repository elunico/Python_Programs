# Thomas Povinelli
# branching.py
# May 18-19, 2015
# 105 minutes
# 2 languages - 1 living; 1 dead
# 32000 successful tests in less than 4 seconds

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

import random

def roll() :
    r = random.randint(2, 13)
    return r;

class person_t(object):
    def __init__(self):
        self.admin = 3; self.bribery = 5; self.leader = 2; self.carousing = 0; self.eng = 0; self.ship_boat = 3; self.prosp = 0; self.vacc_suit = 4; self.nav = 0;

def prospect1(p):
    a = roll() + p.prosp + p.eng + p.vacc_suit
    if a <= 5:
        result = moveToTrojan(p)
    elif a >= 6 and a <= 8:
        result = prospect2(p)
    else:
        result = restAndRec(p)
    return result 
    
def prospect2(p):
    a = roll() + p.prosp + p.eng + p.vacc_suit
    if a <= 8:
        result = prospect1(p)
    elif a >= 9 and a <= 11:
        result = danger(p)
    else:
        result = 3
    return result

def moveToTrojan(p):
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
    a = roll()
    if a < 5:
        result = moveToRRA(p)
    elif a >= 6 and a <= 10:
        result = prospect1(p)
    else:
        result = prospect2(p)
    return result
    

def moveToCurrentProducingArea(p):
    a = roll()
    if a >= 8:
        result = moveToRRA(p)
    elif a <= 7 and a >= 4:
        result = prospect1(p)
    else:
        result = selectAreaOfProspect(p)
    return result


def moveToBeltFringe(p):
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
    a = roll()
    if a >= 6 and a <= 9:
        result = 2
    elif a <= 5:
        result = 4
    else:
        result = prospect2(p)
    return result

def refuel(p):
    a = roll() + p.eng + p.ship_boat
    if a >= 8:
        result = moveToBeltFringe(p)
    else:
        result = danger(p)
    return result
    
def needRefuel(p):
    a = roll()
    if a <= 10:
        result = refuel(p)
    else:
        result = 2
    return result
    
def patronAssists(p):
    a = roll() + p.leader
    if a >= 10:
        result = makeSpecialApplication(p)
    else:
        result = needRefuel(p)
    return result

def selectAreaOfProspect(p) :
    attempt = roll() + p.eng + p.nav;
    if (attempt <= 4) :
        result = moveToTrojan(p)
    elif (attempt >= 5 and attempt <= 8) :
        result = prospect1(p)
    else :
        result = moveToCurrentProducingArea(p)
    return result;

def goNoLicense(p) :
    attempt = roll();
    if (attempt <= 5) :
        result = seekPatron(p);
    else :
        result = selectAreaOfProspect(p);
    return result;

def seekPatron (p) :
    attempt = roll();
    if (attempt <= 4) :
        result = applicationDenied(p);
    elif (attempt >= 5 and attempt >= 8) :
        result = patronAssists(p);
    else :
        result = goNoLicense(p);
    return result;

def makeSpecialApplication(p) :
    attempt = roll(); 
    if (attempt>= 9 ) :
        print("License Granted!")
        result = selectAreaOfProspect(p);
    else :
        result = applicationDenied(p);
    return result;

def considerBribe(p) :
    attempt = roll(); 
    if (attempt >= 8) :
        result = offerBribe(p);
    elif (attempt >=6 and attempt <=7) :
        result = makeSpecialApplication(p) ;
    else :
        result = applicationDenied(p);
    return result;

def offerBribe(p) :
    attempt = roll(); 
    if (attempt <= 5) :
        result = considerBribe(p);
    elif (attempt >= 6 and attempt <= 9) :
        result = apply(p);
    else :
        print("License Granted!")
        result = selectAreaOfProspect(p);
    return result;

def apply(p) :
    apply = roll(); 
    if (apply <= 7) :
        result = applicationDenied(p);
    else :
        result = offerBribe(p);
    return result;

def applicationDenied(p) :
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

def main () :
    p = person_t();
    print("You apply for a license")
    result = apply(p);
    if (result == 1) :
        print("Belting")
    elif result == 2:
        print("Dead")
    elif result == 3:
        print("Strike")
    if result != 3 and result != 1:
        print("End")
    return 0;

if __name__ == '__main__':
    main()