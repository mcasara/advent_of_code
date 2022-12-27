def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def read_all_directories(input):
    current_dir = ['/']
    directories_tree = dict()
    for k in input:
        if k == '$ cd ..':
            current_dir.pop(-1)
        if k[:4] == '$ cd' and k[5:] != '..':
            new_dir = k[5:]
            try:
                directories_tree[current_dir[-1]] = directories_tree[current_dir[-1]] + ', ' + new_dir
            except:
                directories_tree[current_dir[-1]] = new_dir
            current_dir.append(new_dir)
    return directories_tree


def main():
    file = read_input("input_7.txt")
    return print(read_all_directories(file[1:]))
    # return print(f"Part 1: {solve(file[0], 4)}"
    #              f"\nPart 2: {solve(file[0], 14)}")


if __name__ == "__main__":
    main()
