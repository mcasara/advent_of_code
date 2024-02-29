def read_input(file, type):
    content = []
    with open(file, 'r') as f:
        if type == 'float':
            for line in f:
                try:
                    content.append(float(line.strip('\n')))
                except:
                    content.append('null')
        elif type == 'int':
            for line in f:
                try:
                    content.append(int(line.strip('\n')))
                except:
                    content.append('null')
        else:
            for line in f:
                content.append(line.strip('\n'))
    return (content)


import re


def find_code_2(s):
    words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    pattern = re.compile('|'.join(words_to_numbers.keys()))
    i, j = 1, 1
    left_to_right = re.subn(pattern, lambda x: words_to_numbers[x.group()], s[:i])
    right_to_left = re.subn(pattern, lambda x: words_to_numbers[x.group()], s[-j:])
    # Check if replace is successful, or we encounter a number, left to right
    while left_to_right[1] == 0 and not s[i - 1].isnumeric():
        # The position of [-1] in [:i] is [i - 1]
        i += 1
        left_to_right = re.subn(pattern, lambda x: words_to_numbers[x.group()], s[:i])
    # right to left
    while right_to_left[1] == 0 and not s[-j].isnumeric():
        j += 1
        right_to_left = re.subn(pattern, lambda x: words_to_numbers[x.group()], s[-j:])
    first_number = str(left_to_right[0][-1] if not s[i - 1].isnumeric() else s[i - 1])
    second_number = str(right_to_left[0][0] if not s[-j].isnumeric() else s[-j])
    return int(first_number + second_number)


def find_code_1(string):
    i = 0
    n = len(string)
    while not string[i].isnumeric():
        i += 1
    first_number = string[i]
    j = 0
    while not string[n - j - 1].isnumeric():
        j += 1
    second_number = string[-j - 1]
    return int(str(first_number) + str(second_number))


def main():
    txt = read_input("input_1.txt", '')
    sum_1 = 0
    for line in txt:
        sum_1 += find_code_1(line)
    sum_2 = 0
    for line in txt:
        sum_2 += find_code_2(line)
    print('part1:', sum_1)
    print('part2:', sum_2)

    return sum


if __name__ == "__main__":
    main()
