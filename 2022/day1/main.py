import math, sys, os, typing

def main():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
    
    elves = dict()  # elf: calories
    i=0
    elves[i] = 0
    for line in data:
        if line == "":
            i += 1
            elves[i] = 0
            continue
        elves[i] += int(line)

    print("part1: " + str(max(elves.values())))

    sorted = list()
    for item in elves:
        sorted.append(elves[item])
    
    sorted.sort(reverse=True)

    print("part2: " + str(sum(sorted[0:3])))

        
if __name__ == "__main__":
    main()