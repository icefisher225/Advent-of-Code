import math, sys, os, time

def magnitude(char):
    if char.lower() == char:
        return ord(char) - 96
    elif char.upper() == char:
        return ord(char) - 38
    return 0


def match(one, two, three):
    print(f"Matching {one}, {two} and {three}")
    for c1 in one:
        for c2 in two:
            if c1 != c2:
                continue
            for c3 in three:
                if c1 == c2 == c3:
                    return c1

    raise Exception("No match found, tried to match {one}, {two} and {three}")

def main():
    with open("data.txt", "r") as f:
        split_data = f.read().splitlines()

    total = 0

    iter = 0
    for i in range(0, len(split_data), 3):
        print(f"Processing {iter}")
        print(f"{split_data[0]}")
        total += magnitude(match(split_data[i], split_data[i+1], split_data[i+2]))
    
    print(total)



if __name__ == "__main__":
    main()