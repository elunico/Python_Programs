def GCF(n1, n2):
    while n2:
        if n1 > n2:
            n1 -= n2
        elif n2 > n1:
            n2 -= n1
        elif n2 == n1:
            return n1

def main():
    e = raw_input("Please enter the two numbers separated by a space: ")
    while e:
        x, y = [int(i) for i in e.split()]
        print(GCF(x, y))
        e = raw_input("Please enter the two numbers separated by a space: ")

if __name__ == '__main__':
    main()
