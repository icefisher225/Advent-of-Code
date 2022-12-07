import math, sys, time, os

def main():
    with open("2022/day4/data.txt", "r") as f:
        data = f.read().splitlines()
    
    count = 0

    for line in data:
        split = line.split(",")
        first = split[0].split("-")
        second = split[1].split("-")
        first = [int(x) for x in first]
        second = [int(x) for x in second]
        first = range(first[0], first[1] + 1)
        second = range(second[0], second[1] + 1)

        contains = False
        check = False
        for i in first:
            if i in second:
                check = True
            else:
                check = False
                break
        if check:
            count += 1
            continue

        for i in second:
            if i in first:
                check = True
            else:
                check = False
                break
        
        if check:
            count += 1
            continue

    print(count)
        
        

if __name__ == "__main__":
    main()

