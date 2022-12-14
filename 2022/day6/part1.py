import os, sys, math, time

def alldifferent(lst):
    assert len(lst) == 4
    if lst[0] != lst[1] and lst[0] != lst[2] and lst[0] != lst[3]:
        if lst[1] != lst[2] and lst[1] != lst[3]:
            if lst[2] != lst[3]:
                return 0

    return 1


def main():
    fl = "data.txt"
    with open(fl, "r") as f:
        data = f.read()

    for i in range(len(data)-3):
        last4 = [data[i], data[i+1], data[i+2], data[i+3]]
        if not alldifferent(last4):
            print(f"start = {i+}")
            break

if __name__ == "__main__":
    main()