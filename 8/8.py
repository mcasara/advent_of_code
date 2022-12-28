import time


def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def visible(x, y, forest):
    if x == 0 or x == len(forest) - 1:
        return True
    if y == 0 or y == len(forest[0]) - 1:
        return True
    from_east = [int(k) for k in forest[x][:y]]
    if int(forest[x][y]) > max(from_east):
        return True
    from_west = [int(k) for k in forest[x][y + 1:]]
    if int(forest[x][y]) > max(from_west):
        return True
    from_north = [int(k[y]) for k in forest[:x]]
    if int(forest[x][y]) > max(from_north):
        return True
    from_south = [int(k[y]) for k in forest[x + 1:]]
    if int(forest[x][y]) > max(from_south):
        return True
    return False


def count_visible(input):
    x, y = len(input), len(input[0])
    count = 0
    for i in range(x):
        for j in range(y):
            if visible(i, j, input):
                count += 1
    return count


def visible_from(x, y, forest):
    if x == 0 or x == len(forest) - 1:
        return 0
    if y == 0 or y == len(forest[0]) - 1:
        return 0
    to_west = [int(k) for k in forest[x][:y]]
    to_west.reverse()
    i = 0
    view_west = 0
    while i < len(to_west) and to_west[i] < int(forest[x][y]):
        view_west += 1
        i += 1
    if i != len(to_west) or to_west[i - 1] >= int(forest[x][y]):
        view_west += 1
    to_east = [int(k) for k in forest[x][y + 1:]]
    i = 0
    view_east = 0
    while i < len(to_east) and to_east[i] < int(forest[x][y]):
        view_east += 1
        i += 1
    if i != len(to_east) or to_east[i - 1] >= int(forest[x][y]):
        view_east += 1
    to_north = [int(k[y]) for k in forest[:x]]
    to_north.reverse()
    i = 0
    view_north = 0
    while i < len(to_north) and to_north[i] < int(forest[x][y]):
        view_north += 1
        i += 1
    if i != len(to_north) or to_north[i - 1] >= int(forest[x][y]):
        view_north += 1
    to_south = [int(k[y]) for k in forest[x + 1:]]
    i = 0
    view_south = 0
    while i < len(to_south) and to_south[i] < int(forest[x][y]):
        view_south += 1
        i += 1
    if i != len(to_south) or to_south[i - 1] >= int(forest[x][y]):
        view_south += 1
    return view_east * view_west * view_north * view_south


def visible_from_score(input):
    x, y = len(input), len(input[0])
    scores = []
    for i in range(x):
        for j in range(y):
            scores.append(visible_from(i, j, input))
    return (max(scores))


def main():
    file = read_input("input_8.txt")
    return print(f"Part 1: {count_visible(file)}"
                 f"\nPart 2: {visible_from_score(file)}")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    print(time.process_time() - start_time, "seconds")
