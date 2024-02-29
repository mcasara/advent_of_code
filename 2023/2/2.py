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


def check_dict_ok(dict_color):
    return (
            0 < dict_color["red"] <= 12
            and 0 < dict_color["green"] <= 13
            and 0 < dict_color["blue"] <= 14
    )


def update_if_max(number, dict_color, color):
    # Update the dictionary with the highest number of each color seen
    if dict_color[color] < number:
        dict_color[color] = number
    return dict_color


def power_dict_color(dict_color):
    return dict_color["red"] * dict_color["green"] * dict_color["blue"]


def game(input_2):
    game_cycle = 0
    sum_game_1 = 0
    sum_game_2 = 0
    dict_color = {"red": 0, "blue": 0, "green": 0}
    for k in input_2:
        game_cycle += 1
        # Reset dict_color
        dict_color = dict_color.fromkeys(dict_color, 0)
        # Isolate "Game #:" from the drafts
        k_strip_game = k.split(": ")[1]
        # Isolate "# red, # blue, # green" from the shows
        k_strip_game_steps = k_strip_game.split("; ")
        # Isolate "# red", "# blue", "# green" within a show
        k_strip_game_steps_show = [j.split(", ") for j in k_strip_game_steps]
        k_strip_game_steps_show_color = []
        # Union all the "show color" events because they are independent events
        for steps in range(len(k_strip_game_steps_show)):
            k_strip_game_steps_show_color.append(
                [
                    k_strip_game_steps_show[steps][i].split(" ")
                    for i in range(len(k_strip_game_steps_show[steps]))
                ]
            )
        # Update the dictionary with the maximum number of each color seen
        for showed_colors in k_strip_game_steps_show_color:
            for number, color in showed_colors:
                update_if_max(int(number), dict_color, color)
        # Check if the game was possibly played with 12,13,14 red,green,blue cubes
        if check_dict_ok(dict_color):
            sum_game_1 += game_cycle
        # Calculate the power of the sets
        sum_game_2 += power_dict_color(dict_color)

    return sum_game_1, sum_game_2


def main():
    text = read_input("input_2.txt")
    print(game(text))


if __name__ == "__main__":
    main()
