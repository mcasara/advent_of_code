import numpy as np


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


def parse_card(line):
    # Returns a tuple (winning_numbers, played_numbers)
    parsed_1 = line.split(":")
    parsed_2 = parsed_1[1].split("|")
    parsed_3 = (parsed_2[0].split(), parsed_2[1].split())
    return parsed_3


def count_points(card):
    # Given a card, return the score
    exponent = 0
    for number in card[0]:
        if number in card[1]:
            exponent += 1
    if exponent == 0:
        return 0
    else:
        return 2 ** (exponent - 1)


def count_matches(card):
    # Given a card, return the number of matches
    matches = 0
    for number in card[0]:
        if number in card[1]:
            matches += 1
    return matches


def accumulate_from_one(cards):
    # Start from the first card and iterate as follows:
    # 1. Count the number of matches N
    # 2. Append the number of Card #1 to the following N cards
    # 3. Repeat for Card #2 ...
    list_of_number_of_cards = np.ones(len(cards))
    for card in range(len(cards)):
        matches = count_matches(parse_card(cards[card]))
        for match in range(matches):
            list_of_number_of_cards[card + match + 1] += list_of_number_of_cards[card]
    return list_of_number_of_cards


def main():
    input_4 = read_input("input_4.txt")
    sum_1 = 0
    for line in input_4:
        sum_1 += count_points(parse_card(line))
    print("part_1: ", sum_1)
    sum_2 = sum(accumulate_from_one(input_4))
    print("part_2: ", sum_2)


if __name__ == "__main__":
    main()
