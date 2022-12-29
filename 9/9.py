import time


def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def head_tail_up(coordinate_h, coordinate_t):
    x_h, y_h = coordinate_h
    x_t, y_t = coordinate_t
    if x_h == x_t and y_t == y_h + 1:  # tail below
        coordinate_t[1] -= 1
    elif y_t == y_h + 1 and (
            x_t == x_h - 1 or x_t == x_h + 1):  # tail down left or down right
        coordinate_t = [x_h, y_h]
    coordinate_h[1] -= 1
    return [coordinate_h, coordinate_t]


def head_tail_down(coordinate_h, coordinate_t):
    x_h, y_h = coordinate_h
    x_t, y_t = coordinate_t
    if x_h == x_t and y_t == y_h - 1:  # tail above
        coordinate_t[1] += 1
    elif y_t == y_h - 1 and (
            x_t == x_h - 1 or x_t == x_h + 1):  # tail up left or up right
        coordinate_t = [x_h, y_h]
    coordinate_h[1] += 1
    return [coordinate_h, coordinate_t]


def head_tail_left(coordinate_h, coordinate_t):
    x_h, y_h = coordinate_h
    x_t, y_t = coordinate_t
    if x_t == x_h + 1 and y_t == y_h:  # tail right
        coordinate_t[0] -= 1
    elif x_t == x_h + 1 and (
            y_t == y_h - 1 or y_t == y_h + 1):  # tail up right or down right
        coordinate_t = [x_h, y_h]
    coordinate_h[0] -= 1
    return [coordinate_h, coordinate_t]


def head_tail_right(coordinate_h, coordinate_t):
    x_h, y_h = coordinate_h
    x_t, y_t = coordinate_t
    if x_t == x_h - 1 and y_t == y_h:  # tail left
        coordinate_t[0] += 1
    elif x_t == x_h - 1 and (
            y_t == y_h - 1 or y_t == y_h + 1):  # tail up left or down left
        coordinate_t = [x_h, y_h]
    coordinate_h[0] += 1
    return [coordinate_h, coordinate_t]


def path(input):
    coordinate_t = [0, 0]
    coordinate_h = [0, 0]
    trail_dict = dict()
    for k in input:
        sp = k.split(' ')
        if sp[0] == 'U':
            for i in range(int(sp[1])):
                new_coordinates = head_tail_up(coordinate_h, coordinate_t)
                coordinate_h, coordinate_t = new_coordinates
                trail_dict[str(coordinate_t)] = 1
        elif sp[0] == 'L':
            for i in range(int(sp[1])):
                new_coordinates = head_tail_left(coordinate_h, coordinate_t)
                coordinate_h, coordinate_t = new_coordinates
                trail_dict[str(coordinate_t)] = 1
        elif sp[0] == 'D':
            for i in range(int(sp[1])):
                new_coordinates = head_tail_down(coordinate_h, coordinate_t)
                coordinate_h, coordinate_t = new_coordinates
                trail_dict[str(coordinate_t)] = 1
        elif sp[0] == 'R':
            for i in range(int(sp[1])):
                new_coordinates = head_tail_right(coordinate_h, coordinate_t)
                coordinate_h, coordinate_t = new_coordinates
                trail_dict[str(coordinate_t)] = 1
    return len(trail_dict)


def main():
    file = read_input("input_9.txt")
    print(path(file))


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    print(time.process_time() - start_time, "seconds")
