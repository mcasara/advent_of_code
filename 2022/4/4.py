def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n').split(','))
    return content


def parse_list(file_input):
    count = 0
    for k in file_input:
        a_0, b_0 = k[0].split('-')
        a_1, b_1 = k[1].split('-')
        if int(a_0) <= int(a_1) and int(b_0) >= int(b_1):
            count += 1
        elif int(a_1) <= int(a_0) and int(b_1) >= int(b_0):
            count += 1
    return count


def parse_list_2(file_input):
    count = 0
    for k in file_input:
        a_0, b_0 = k[0].split('-')
        a_1, b_1 = k[1].split('-')
        if int(b_0) < int(a_1):
            count += 0
        elif int(a_0) > int(b_1):
            count += 0
        else:
            count += 1
    return count


def main():
    file = read_input("input_4b.txt")
    return print(f"Part 1: {parse_list(file)} "
                 f"Part 2: {parse_list_2(file)}")


if __name__ == "__main__":
    main()
