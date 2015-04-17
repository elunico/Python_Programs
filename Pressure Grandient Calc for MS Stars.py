from __future__ import division
try:
    from Tkinter import *
except ImportError: # Python 3 Catch
    try:
        from tkinter import *
    except ImportError:
        print("Sorry, you need Tkinter for this program to function")
        raise SystemExit

def heq(limit = 45, radius = 23193333, density=4.5, step=45000000):
    basemass = 10
    exponent = 1
    total = 0
    pressures = []
    while exponent <= limit:
        try:
            pressure = (((6.6738 * (10 ** -11)) * (basemass ** exponent)) / ((radius ** 2))) * density
        except OverflowError:
            error = Tk()
            error.title("Error")
            error.geometry("+60+20")
            Label(error, text="Overflow Error").pack()
            Label(error, text="Please Check your Numbers").pack()
            Button(error, text="close", command=error.destroy).pack()
            error.mainloop()
            return None, None # Return none and none instead of negatives because I'm not a physicist and I don't know if 1 and 0 may be valid answers
        pressures.append(pressure)
        total += pressure
        exponent += 1
        radius += step
    return total, pressures

class Application(object):
    def __init__(self):
        pass
    def main(self):
        self.root = Tk()
        self.root.title("Pressure Gradient Calculator")
        self.root.geometry("+100+30")
        self.l1 = Label(self.root, text="Enter the limit (45 by default): ")
        self.l2 = Label(self.root, text="Enter the radius (Solar Radius by default): ")
        self.l3 = Label(self.root, text="Enter the density (4.5 by default): ")
        self.l4 = Label(self.root, text="Enter the steps (45,000,000 by default): ")
        self.e1 = Entry(self.root)
        self.e2 = Entry(self.root)
        self.e3 = Entry(self.root)
        self.e4 = Entry(self.root)
        self.b1 = Button(self.root, text="Go", command=self.calc)
        self.l1.grid(row=0, column=0, padx=5, pady=5)
        self.l2.grid(row=1, column=0, padx=5, pady=5)
        self.l3.grid(row=2, column=0, padx=5, pady=5)
        self.l4.grid(row=3, column=0, padx=5, pady=5)
        self.e1.grid(row=0, column=1, padx=5, pady=5)
        self.e2.grid(row=1, column=1, padx=5, pady=5)
        self.e3.grid(row=2, column=1, padx=5, pady=5)
        self.e4.grid(row=3, column=1, padx=5, pady=5)
        self.b1.grid(row=4, column=1, padx=5, pady=5)
        self.root.mainloop()
    def calc(self):

        l = self.e1.get()
        r = self.e2.get()
        d = self.e3.get()
        s = self.e4.get()
        try:
            l = float(l)
        except:
            l = 45
        try:
            r = float(r)
        except:
            r = 23193333
        try:
            d = float(d)
        except:
            d = 4.5
        try:
            s = float(s)
        except:
            s = 45000000
        if r == 0:
            answer = Tk()
            answer.title("Results")
            answer.geometry("+60+20")
            Label(answer, text="Cannot have 0 radius!").pack()
            Label(answer, text="Division by Zero Error").pack()
            return "Error"

        total, pressures = heq(l, r, d, s)
        if total == None and pressures == None:
            return -1
        try:
            if answer:
                pass
        except:
            answer = Tk()
            answer.title("Results")
            answer.geometry("+60+20")
        row = 0
        col = 0
        for i in pressures:
            Label(answer, text=i, font=("Courier New", "14", "normal")).grid(row=row, column=col, padx=5, pady=5)
            row += 1
            if row == 18:
                col += 1
                row = 0
        Label(answer, text="Total:", font=("Courier New", "14", "bold")).grid(row=row, column=col)
        row += 1
        Label(answer, text=total, font=("Courier New", "14", "bold")).grid(row=row, column=col)
        if row == 18:
            col += 1
            row = 0
        Button(answer, text="Close", command=answer.destroy).grid(row=row+1, column=col)
        answer.mainloop()

def main():
    h = Application()
    result = h.main()
    while result == "Error":
        h.main()

if __name__ == '__main__':
    main()