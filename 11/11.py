import time
from math import floor


def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.operator = ''
        self.operand = ''
        self.divisibility = 1
        self.throw_to = []
        self.inspect_number = 0


def monkey_function(monkey, item, part):
    worry = item
    if monkey.operator == '*':
        if monkey.operand == 'old':
            worry *= worry
        else:
            worry *= int(monkey.operand)
    elif monkey.operator == '+':
        if monkey.operand == 'old':
            worry += worry
        else:
            worry += int(monkey.operand)
    if part == 1:
        worry = worry//3
    if worry % monkey.divisibility == 0:
        throw_to = monkey.throw_to[0]
    else:
        throw_to = monkey.throw_to[1]
    return [worry, throw_to]

def round(input, part, n):
    zoo = create_zoo(input)
    a=0
    for i in range (n):
        for mk in range(8):
            for item in zoo[mk].items:
                zoo[mk].inspect_number += 1
                item_to_throw, throw_to = monkey_function(zoo[mk], item, part)
                zoo[throw_to].items.append(item_to_throw)
            zoo[mk].items = []
        if i % 100 == 0:
            print( f"{1*a} % done")
            a+=1
    return zoo


def create_zoo(input):
    number_of_monkeys = 8
    chunks = [input[7 * k: 7 + 7 * k]
              for k in range(number_of_monkeys)]
    zoo = [Monkey(f"Monkey {k}") for k in range(number_of_monkeys)]
    i = 0
    for k in chunks:
        zoo[i].items = [int(i) for i in k[1][18:].split(', ')]
        zoo[i].operator, zoo[i].operand = k[2][23], k[2][25:]
        zoo[i].divisibility = int(k[3][21:])
        zoo[i].throw_to = [int(k[4][29:]), int(k[5][30:])]
        i += 1
    return zoo


def main():
    file = read_input("input_11.txt")
    liste_inspect = [i.inspect_number for i in round(file, 1, 20)]
    liste_inspect.sort(reverse = True)
    # liste_inspect_2 = [i.inspect_number for i in round(file, 2, 10000)]
    # liste_inspect_2.sort(reverse = True)
    return print(f"Part 1: {liste_inspect[0] * liste_inspect[1]}")
                 # f"\nPart 2: {liste_inspect_2[0] * liste_inspect_2[1]}")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    print(time.process_time() - start_time, "seconds")
