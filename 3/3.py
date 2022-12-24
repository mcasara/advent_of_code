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


def transform_input(list_input):
    result = []
    for k in list_input:
        a, b = halve_list(k)
        result.append(points((intersection(a, b))[0]))
    return result


def main():
    file = read_input("input_3.txt")
    return print(sum(transform_input(file)))


if __name__ == "__main__":
    main()
