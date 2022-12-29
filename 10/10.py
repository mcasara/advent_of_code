import time


def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def parse_cycle(input, part):
    cycles_V = []
    add_V = 0
    for k in input:
        if k == 'noop':
            try:
                cycles_V.append(cycles_V[-1] + add_V)
                add_V = 0
            except:
                cycles_V.append(1)
        else:
            try:
                cycles_V.append(cycles_V[-1] + add_V)
                cycles_V.append(cycles_V[-1])
                add_V = int(k.split(' ')[1])
            except:
                cycles_V.append(1)
                cycles_V.append(cycles_V[-1])
                add_V = int(k.split(' ')[1])
    cycles_V.append(cycles_V[-1] + add_V)
    str = [20 + 40 * k - 1 for k in range(6)]
    if part == 1:
        return sum([(k + 1) * cycles_V[k] for k in str])
    else:
        big_list = []
        for k in range(240):
            if k % 40 in [cycles_V[k] - 1, cycles_V[k], cycles_V[k] + 1]:
                big_list.append('#')
            else:
                big_list.append('.')
    chunks_big_list = [big_list[40 * k:40 + 40 * k] for k in range(6)]
    return print(f"{chunks_big_list[0]}\n"
                 f"{chunks_big_list[1]}\n"
                 f"{chunks_big_list[2]}\n"
                 f"{chunks_big_list[3]}\n"
                 f"{chunks_big_list[4]}\n"
                 f"{chunks_big_list[5]}\n")


def main():
    file = read_input("input_10.txt")
    return print(f"Part 1: {parse_cycle(file,1)}"
                 f"\nPart 2: {parse_cycle(file,2)}")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    print(time.process_time() - start_time, "seconds")
