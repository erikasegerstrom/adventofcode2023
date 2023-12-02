class Game():
    def __init__(self, id) -> None:
        self.id = id
        self.n_blue = 0
        self.n_green = 0
        self.n_red = 0

games = []

with open('inputs/day2.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip() #remove newline char
        game_index = line.split(":")[0].split(" ")[1]
        sets = line.split(":")[1:]
        split_sets = sets[0].split(";")

        """ Construct game """
        game = Game(game_index)
        for set in split_sets:
            for pick in set.split(","):
                pick_colour = pick.split(" ")[2]
                pick_number = int(pick.split(" ")[1])
                if pick_colour == "green":
                    game.n_green = max(pick_number, game.n_green)
                elif pick_colour == "red":
                    game.n_red = max(pick_number, game.n_red)
                elif pick_colour == "blue":
                    game.n_blue = max(pick_number, game.n_blue)

        games.append(game)
        

id_sum_of_valid_games = 0
power_sum = 0
for game in games:
    if (game.n_green <= 13 and game.n_red <= 12 and  game.n_blue <= 14):
        id_sum_of_valid_games += int(game.id)
    power_sum += (game.n_green * game.n_red * game.n_blue)

print("Number of valid games: ", id_sum_of_valid_games)
print("Power sum: ", power_sum)