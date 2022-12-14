import math, typing, re

class Stack:
    def __init__(self, location):
        self.stack = []
        self.loc = location

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def location(self):
        return self.loc

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        out = f"{self.loc} | "
        for item in self.stack[::-1]:
            out += item.__str__() + " "
        return out

class Crane:
    def __init__(self, yard: typing.List[Stack]):
        self.location = 0
        self.yard = yard

    def goto(self, location):
        self.location = location

    def move(self, num, start, stop):
        for i in range(num):
            temp = self.yard[start].pop()
            self.yard[stop].push(temp)

class Crate:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value

    def __str__(self):
        return f"{self.value}"

def main():
    yard = [Stack(i) for i in range(1, 10)]

    with open("2022/day5/data.txt", "r") as f:
        data = f.read().splitlines()

    initmap = []
    for i in range(10):
        initmap.append(list())

    for i in range(0, 10):
        for j in range(0, len(data[i]), 4):
            initmap[i].append(data[i][j:j+3])

    '''
    # Prints data before processing into stacks
    for item in initmap:
        for part in item:
            print(f"{part} ", end='')
        print()
    '''

    for i in range(8):
        for j in range(9):
            yard[j].push(Crate(str(initmap[i][j])))

    print(f"\nInitial Yard: \n")
    for stack in yard:
        print(stack.__str__())
    print()

    # Create Crane
    crane = Crane(yard)
    for i in range(10, len(data)):
        line = data[i]
        line = line.split(" ")
        instructions = []
        for part in line: 
            if part.isnumeric():
                instructions.append(int(part))
        
        crane.move(instructions[0], instructions[1], instructions[2])

    print(f"\nFinal Yard: \n")
    for stack in yard:
        print(stack.__str__())
    print()


if __name__ == "__main__":
    main()