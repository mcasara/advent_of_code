def read_input(file):
    content = []
    with open(file, 'r') as f:
        for line in f:
            content.append(line.strip('\n'))
    return content


# [M] [H]         [N]
# [S] [W]         [F]     [W] [V]
# [J] [J]         [B]     [S] [B] [F]
# [L] [F] [G]     [C]     [L] [N] [N]
# [V] [Z] [D]     [P] [W] [G] [F] [Z]
# [F] [D] [C] [S] [W] [M] [N] [H] [H]
# [N] [N] [R] [B] [Z] [R] [T] [T] [M]
# [R] [P] [W] [N] [M] [P] [R] [Q] [L]
# 1   2   3   4   5   6   7   8   9

def solve(input):
    _input = ['MSJLVFNR', 'HWJFZDNP', 'GDCRW', 'SBN', 'NFBCPWZM', 'WMRP', 'WSLGNTR',
              'VBNFHTQ', 'FNZHML']
    _input_list = [list(k) for k in _input]
    for i in input:
        for k in range(int(i[0])):
            move = _input_list[int(i[1]) - 1].pop(0)
            _input_list[int(i[2]) - 1].insert(0, move)
    return _input_list


def solve_2(input):
    _input = ['MSJLVFNR', 'HWJFZDNP', 'GDCRW', 'SBN', 'NFBCPWZM', 'WMRP', 'WSLGNTR',
              'VBNFHTQ', 'FNZHML']
    _input_list = [list(k) for k in _input]
    for i in input:
        move = _input_list[int(i[1]) - 1][:int(i[0])]
        _input_list[int(i[1]) - 1] = _input_list[int(i[1]) - 1][int(i[0]):]
        _input_list[int(i[2]) - 1] = move + _input_list[int(i[2]) - 1]
    return _input_list


def main():
    file = read_input("input_5.txt")
    file_input = [
        k.replace('move ', '').replace('from ', '').replace('to ', '').replace(' ',
                                                                               ',').split(
            ',') for k in file[10:]]
    final_position = solve(file_input)
    final_position_2 = solve_2(file_input)
    return print(f"Part 1: {''.join([k[0] for k in final_position])}"
                 f"\nPart 2: {''.join([k[0] for k in final_position_2])}")


if __name__ == "__main__":
    main()
