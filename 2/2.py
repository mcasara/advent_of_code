def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def map_content(content):
    for i in range(len(content)):
        if content[i] == 'X' or content[i] == 'A':
            content[i] = 1
        elif content[i] == 'Y' or content[i] == 'B':
            content[i] = 2
        elif content[i] == 'Z' or content[i] == 'C':
            content[i] = 3
    return content


def parse_content(content):
    adv = [k[0] for k in content]
    me = [k[2] for k in content]
    return map_content(adv), map_content(me)


def points_part_1(l1, l2):
    point = []
    for k in range(len(l1)):
        if l1[k] == l2[k]:
            point.append(3)
        elif l1[k] == 1:
            if l2[k] == 2:
                point.append(6)
            else:
                point.append(0)
        elif l1[k] == 2:
            if l2[k] == 3:
                point.append(6)
            else:
                point.append(0)
        elif l1[k] == 3:
            if l2[k] == 1:
                point.append(6)
            else:
                point.append(0)
    return point


def points_part_2(l1, l2):
    point = []
    for k in range(len(l1)):
        if l2[k] == 2:
            point.append(3 + l1[k])
        elif l2[k] == 1:
            if l1[k] == 1:
                point.append(0 + 3)
            elif l1[k] == 2:
                point.append(0 + 1)
            else:
                point.append(0 + 2)
        elif l2[k] == 3:
            if l1[k] == 1:
                point.append(6 + 2)
            elif l1[k] == 2:
                point.append(6 + 3)
            else:
                point.append(6 + 1)
    return point


def main():
    adv, me = parse_content(read_input("input_2.txt"))
    return print(
        f"Part 1: {sum(points_part_1(adv, me)) + sum(me)}"
        f"\nPart 2: {sum(points_part_2(adv, me))}")


if __name__ == "__main__":
    main()
