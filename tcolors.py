'''Printing these constants will
change to the indicated color until 
otherwise specified by a new color

You can also call the functions to
make the colors change that way'''

magenta = purple = '\033[95m'
blue = '\033[94m'
green = _pass = Pass = ok = '\033[92m'
yellow = warn = warning = '\033[93m'
red = error = fail = '\033[91m'
end = clear_color = clear = black = '\033[0m'
bold = strong = '\033[1m'
underline = uline = '\033[4m'

colors = {'magenta':magenta, 'purple':purple, 'blue':blue, 'green':green, '_pass':_pass, 'Pass':Pass, 'ok':ok,
           'yellow':yellow, 'warn':warn, 'warning':warning, 'red':red, 'error':error, 'fail':fail}

styles = {'bold':bold, 'strong':strong, 'underline':underline, 'uline':uline}

def changecolor(color):
    c = color.lower().strip()
    try:
        print(colors[c])
    except KeyError:
        print ("You must choose from {}".format(list(colors.keys())))
        return 1

def clearall():
    print (end)

def makebold():
    print (bold)

def makeunderline():
    print (underline)