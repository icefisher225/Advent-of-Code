import math, sys, os, time

def magnitude(char):
    if char.lower() == char:
        return ord(char) - 96
    elif char.upper() == char:
        return ord(char) - 38
    return 0


def match(chars, string):
    print(f"Matching {chars} with {string}")
    for char in chars:
        print(f"Matching {char} with {string}")
        if char in string:
            return char

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
    for item in split_data:
        print(f"Processing {iter}")
        print(f"{split_data[0]}")
        total += magnitude(match(item[0], item[1]))
        iter += 1

    print(total)



if __name__ == "__main__":
    main()