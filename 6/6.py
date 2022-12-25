def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def solve(input, size):
    i = 0
    end = False
    while not end and i <= len(input):
        end = len(set(input[i:(i + size)])) == size
        i += 1
    return i + size - 1


def main():
    file = read_input("input_6.txt")
    return print(f"Part 1: {solve(file[0], 4)}"
                 f"\nPart 2: {solve(file[0], 14)}")


if __name__ == "__main__":
    main()
