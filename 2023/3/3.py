import re


def read_input(file, file_type=""):
    content = []
    with open(file, "r") as f:
        if file_type == "float":
            for line in f:
                try:
                    content.append(float(line.strip("\n")))
                except:
                    content.append("null")
        elif file_type == "int":
            for line in f:
                try:
                    content.append(int(line.strip("\n")))
                except:
                    content.append("null")
        else:
            for line in f:
                content.append(line.strip("\n"))
    return content


def find_number_and_position(line, j):
    # Replace all non-numerics in the line to whitespaces and split the list
    # Gives for e.g. ['756', '436', '425',...]
    numbers = list(set(re.sub("[^0-9]", " ", line).split()))
    number_position = []
    for number in numbers:
        # Find the position (x, y) of each number in the original line
        number_position.append(
            [
                (number, (m.start(0), j))
                for m in re.finditer(r"\b(" + number + r")\b", line)
            ]
        )
    # Format to [(number, (x, y)), ...]
    return [item for sublist in number_position for item in sublist]


def find_indices(list_to_check, item_to_find):
    # Used when the item to find in a string is of length 1
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def find_symbol_and_position(line, j):
    # As is done for numbers, do the same for symbols (without storing the actual
    # symbol)
    symbols = list(set(re.sub("[0-9]|\\.", " ", line).split()))
    symbol_position = []
    for symbol in symbols:
        symbol_position.append([(i, j) for i in find_indices(line, symbol)])
    # Format to [(x, y), ...]
    return [item for sublist in symbol_position for item in sublist]


def find_star_symbol_and_position(line, j):
    # Same as above but filter on star symbol
    symbols = list(set(re.sub("[0-9]|\\.", " ", line).split()))
    symbol_position = []
    for symbol in symbols:
        if symbol == "*":
            symbol_position.append([(i, j) for i in find_indices(line, symbol)])
    # Format to [(x, y), ...]
    return [item for sublist in symbol_position for item in sublist]


def generate_number_position_matrix(input_3):
    # Parse all lines for numbers and flatten the matrix
    matrix = []
    j = 0
    for line in input_3:
        matrix.append(find_number_and_position(line, j))
        j += 1
    # Flatten the matrix
    return [item for sublist in matrix for item in sublist]


def generate_symbol_position_matrix(input_3):
    # Parse all lines for symbols and flatten the matrix
    matrix = []
    j = 0
    for line in input_3:
        matrix.append(find_symbol_and_position(line, j))
        j += 1
    # Flatten the matrix
    return [item for sublist in matrix for item in sublist]


def generate_star_symbol_position_matrix(input_3):
    matrix = []
    j = 0
    for line in input_3:
        matrix.append(find_star_symbol_and_position(line, j))
        j += 1
    return [item for sublist in matrix for item in sublist]


def is_neighbor_with_symbol(positions, symbol_matrix, number, part):
    # True/False a symbol is in the neighborhood of a number
    is_neighbor = False
    neighborhood = [
        (positions[0] - 1, positions[1]),  # left
        (positions[0], positions[1] - 1),  # up
        (positions[0], positions[1] + 1),  # down
        (positions[0] - 1, positions[1] - 1),  # left up
        (positions[0] - 1, positions[1] + 1),  # left down
    ]
    # A 2 digit number has a larger neighborhood than a single digit number
    for number_length in range(len(number)):
        neighborhood.append((positions[0] + number_length + 1, positions[1]))  #
        # right once, twice or thrice depending on the number of digits
        neighborhood.append(
            (positions[0] + number_length + 1, positions[1] + 1)
        )  # up right once, twice or thrice depending on the number of digits
        neighborhood.append(
            (positions[0] + number_length + 1, positions[1] - 1)
        )  # down right once, twice or thrice depending on the number of digits
    for i in neighborhood:
        if part == "part_1":
            if i in symbol_matrix:
                is_neighbor = True
                break
        if part == "part_2":
            if i == symbol_matrix:
                is_neighbor = True
                break
    return is_neighbor


def number_neighbor_with_symbol(number_position_matrix, symbol_matrix):
    # Parse all the lines and find the numbers with symbols in their neighborhood
    list_to_sum = []
    for number_position in number_position_matrix:
        if is_neighbor_with_symbol(
            number_position[1], symbol_matrix, number_position[0], "part_1"
        ):
            list_to_sum.append(int(number_position[0]))
    return list_to_sum


def number_neighbor_with_star_symbol(number_position_matrix, star_symbol_position):
    # Parse all the lines and find the numbers with "star_symbol_position" in their
    # neighborhood
    list_to_sum = []
    # number_position stores (number, (position_x, position_y))
    for number_position in number_position_matrix:
        if is_neighbor_with_symbol(
            number_position[1], star_symbol_position, number_position[0], "part_2"
        ):
            list_to_sum.append(int(number_position[0]))
    return list_to_sum


def main():
    input_3 = read_input("input_3.txt")
    symbol_matrix = generate_symbol_position_matrix(input_3)
    number_position_matrix = generate_number_position_matrix(input_3)
    print(
        "part1: ",
        sum(number_neighbor_with_symbol(number_position_matrix, symbol_matrix)),
    )
    star_symbol_matrix = generate_star_symbol_position_matrix(input_3)
    sum_gears = 0
    for k in star_symbol_matrix:
        neighbor_to_star_symbol = number_neighbor_with_star_symbol(
            number_position_matrix, k
        )
        if len(neighbor_to_star_symbol) == 2:
            sum_gears += neighbor_to_star_symbol[0] * neighbor_to_star_symbol[1]
    print("part2:", sum_gears)


if __name__ == "__main__":
    main()
