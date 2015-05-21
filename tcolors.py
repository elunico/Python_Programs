'''Printing these constants will
change to the indicated color until 
otherwise specified by a new color'''

__all__ = ['magenta', 'purple', 'blue', 'green', '_pass', 'Pass', 'ok',
           'yellow', 'warn', 'warning', 'red', 'error', 'fail', 'end',
           'clear_color', 'clear', 'bold', 'underline', 'uline', 
           'strong']

magenta = purple = '\033[95m'
blue = '\033[94m'
green = _pass = Pass = ok = '\033[92m'
yellow = warn = warning = '\033[93m'
red = error = fail = '\033[91m'
end = clear_color = clear = '\033[0m'
bold = strong = '\033[1m'
underline = uline = '\033[4m'

