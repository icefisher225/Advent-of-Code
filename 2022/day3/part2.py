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

    raise Exception("No match found")

def main():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
    
    split_data = list()

    for i in range(len(data)):
        d_len = len(data[i])
        split_data.append(list())
        split_data[i].append(data[i][0:d_len//2])
        split_data[i].append(data[i][d_len//2:d_len])
        if len(split_data[i][0]) != len(split_data[i][1]):
            raise Exception("Data not split correctly")
        if split_data[i][0]+split_data[i][1] != data[i]:
            raise Exception("Data not split correctly")

    total = 0

    iter = 0
    for i in range(0, len(split_data), 3):
        print(f"Processing {iter}")
        print(f"{split_data[0]}")
        total += magnitude(match(split_data[i], split_data[i+1], split_data[i+2]))
    
    print(total)



if __name__ == "__main__":
    main()