import math, sys, time, os

def main():
    with open("2022/day4/data.txt", "r") as f:
        data = f.read().splitlines()
    
    count = 0

    splitlist = []

    for line in data:
        split = line.split(",")
        first = split[0].split("-")
        second = split[1].split("-")
        first = [int(x) for x in first]
        second = [int(x) for x in second]
        splitlist.append([range(first[0], first[1] + 1), range(second[0], second[1] + 1)])

    for first, second in splitlist:
        for i in first:
            if i in second:
                count += 1
                break

    print(count)
        
        

if __name__ == "__main__":
    main()

