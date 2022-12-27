import time


def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


def read_all_directories(input, part):
    current_dir = ['root']
    directories_tree = dict()
    directories_size = dict({'root': 0})
    k = 0
    while k < len(input):
        if input[k] == '$ cd ..':
            current_dir.pop(-1)
        if input[k][:4] == '$ cd' and input[k][5:] != '..':
            new_dir = input[k][5:]
            string_dir = '/'.join(current_dir)
            try:
                directories_tree[string_dir] = directories_tree[
                                                   string_dir] + ', ' + '/'.join(
                    current_dir + [new_dir])
            except:
                directories_tree[string_dir] = '/'.join(current_dir + [new_dir])
            current_dir.append(new_dir)
            string_new_dir = '/'.join(current_dir)
            if string_new_dir not in directories_size:
                directories_size[string_new_dir] = 0
            k += 1
            while k < len(input) and input[k][:4] != '$ cd':
                if input[k][0] != '$' and input[k][:3] != 'dir':
                    directories_size[string_new_dir] += int(input[k].split(' ')[0])
                k += 1
            k -= 1
        k += 1
    list_dir = [k.split('/') for k in list(directories_tree.keys())]
    length = 0
    for k in list_dir:
        if len(k) > length:
            length = len(k)
    while length > -1:
        for items in list_dir:
            directory = '/'.join(items)
            if len(items) == length:
                directories_size[directory] += sum(
                    [directories_size[k] for k in
                     directories_tree[directory].split(', ')])
        length -= 1
    if part == 1:
        return sum([k if k < 100000 else 0 for k in list(directories_size.values())])
    else:
        treshold = directories_size['root']-40000000
        return treshold+min([k-treshold if k>treshold else 10000000 for k in list(directories_size.values())])

def main():
    file = read_input("input_7.txt")
    return print(f"Part 1: {read_all_directories(file[1:], 2)}")
    #              f"\nPart 2: {solve(file[0], 14)}")


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    print(time.process_time() - start_time, "seconds")
