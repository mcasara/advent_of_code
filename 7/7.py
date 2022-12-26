def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def main():
    file = read_input("input_7.txt")
    return print(file)
    # return print(f"Part 1: {solve(file[0], 4)}"
    #              f"\nPart 2: {solve(file[0], 14)}")


if __name__ == "__main__":
    main()
