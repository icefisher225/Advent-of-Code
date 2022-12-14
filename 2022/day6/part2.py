import os, sys, math, time

def alldifferent(inpt):
    copy = []
    lst = []
    
    for char in inpt:
        lst.append(char)

    for item in lst:
        copy.append(item)

    listlen = len(lst)

    try:
        for i in range(listlen-1, 0, -1):
            print(f"attempting to remove {lst[i]} from {copy}")
            copy.remove(lst[i])
            if lst[i] in copy:
                return 1
    except Exception as e:
        print(e)
        exit()

    return 0


def main():
    fl = "data.txt"
    with open(fl, "r") as f:
        data = f.read()

    for i in range(len(data)-13):
        last = data[i:i+14]
        print(last)
        if not alldifferent(last):
            print(f"start = {i+14}") #may be wrong
            break

if __name__ == "__main__":
    main()