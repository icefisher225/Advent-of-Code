import math

def main():
    for i in range(1, 100, 1):
        lst = list()
        collatz(i, lst)
        print(lst)

def collatz(i, lst):
    lst.append(i)
    if i == 1:
        return lst
    elif i%2 == 0:
        return collatz(int(i/2), lst)
    else:
        return collatz(3*i+1, lst)

if __name__ == "__main__":
    main()