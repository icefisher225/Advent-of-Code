import math, time, os, sys, random, typing

def Win(score):
    return score + 6

def Loss(score):
    return score + 0

def Tie(score):
    return score + 3


def otherPoints(hand, score):
    if hand == "X":
        return score + 1
    elif hand == "Y":
        return score + 2
    elif hand == "Z":
        return score + 3
    else: 
        raise ValueError("Invalid hand")


def main():
    score = 0
    data = list()
    with open("data.txt", "r") as f:
        for line in f:
            data.append(line.strip().split(" "))

    lut = list() # This will be a list of lists, where list[X] is a possible key 
                 # and list[X][Y] is the function/score to be used for that key
    # A = Rock
    # B = Paper
    # C = Scissors

    # X = Lose
    # Y = Tie
    # Z = Win
    
    lut.append([['A', 'X'], Loss, 3])
    lut.append([['A', 'Y'], Tie, 1])
    lut.append([['A', 'Z'], Win, 2])

    lut.append([['B', 'X'], Loss, 1])
    lut.append([['B', 'Y'], Tie, 2])
    lut.append([['B', 'Z'], Win, 3])

    lut.append([['C', 'X'], Loss, 2])
    lut.append([['C', 'Y'], Tie, 3])
    lut.append([['C', 'Z'], Win, 1])

    for item in data:
        for entry in lut:
            if item == entry[0]:
                score = entry[1](score)
                score += entry[2] # Points for choice


    print(score)



if __name__ == "__main__":  
    main()