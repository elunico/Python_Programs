'''Printing these constants will
change to the indicated color until 
otherwise specified by a new color

You can also call the functions to
make the colors change that way'''

__all__ = ['magenta', 'purple', 'blue', 'green', '_pass', 'Pass', 'ok',
           'yellow', 'warn', 'warning', 'red', 'error', 'fail', 'end',
           'clear_color', 'clear', 'bold', 'underline', 'uline', 
           'strong', 'colors', 'changeColor', 'clearAll', 'makeBold', 'makeUnderline']

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

def changeColor(color):
    c = color.lower().strip()
    try:
        assert c in colors.keys()
    except AssertionError:
        print ("You must choose from {}".format(list(colors.keys())))
        return 1
    print (colors[c])

def clearAll():
    print (end)

def makeBold():
    print (bold)

def makeUnderline():
    print (underline)