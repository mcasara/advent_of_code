def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def points(string):
    if string.isupper():
        return ord(string) - 38
    else:
        return ord(string) - 96


def halve_list(input):
    n = len(input) // 2
    return input[:n], input[n:]


def intersection(input_1, input_2):
    return list(set(input_1).intersection(set(input_2)))[0]


def intersection_2(input_1, input_2, input_3):
    intersect_1 = set(input_1).intersection(set(input_2))
    intersect_2 = intersect_1.intersection(set(input_3))
    return list(intersect_2)[0]


def transform_input(list_input):
    result = []
    for k in list_input:
        a, b = halve_list(k)
        result.append(points((intersection(a, b))))
    return result


def transform_input_2(list_input):
    result = []
    i = 0
    while i < len(list_input)-2:
        a, b, c = list_input[i], list_input[i + 1], list_input[i + 2]
        result.append(points((intersection_2(a, b, c))))
        i += 3
    return result


def main():
    file = read_input("input_3.txt")
    return print(f"Part 1:{sum(transform_input(file))}",
                 f"Part 2: {sum(transform_input_2(file))}")


if __name__ == "__main__":
    main()
