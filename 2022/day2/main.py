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
    # A, X = Rock
    # B, Y = Paper
    # C, Z = Scissors
    
    lut.append([['A', 'X'], Tie])
    lut.append([['B', 'Y'], Tie])
    lut.append([['C', 'Z'], Tie])

    lut.append([['A', 'Y'], Win])
    lut.append([['B', 'Z'], Win])
    lut.append([['C', 'X'], Win])

    lut.append([['A', 'Z'], Loss])
    lut.append([['B', 'X'], Loss])
    lut.append([['C', 'Y'], Loss])


    for item in data:
        score = otherPoints(item[1], score) # TODO: add points for choice
        for i in lut:
            if item == i[0]:
                score = i[1](score)


    print(score)



if __name__ == "__main__":  
    main()