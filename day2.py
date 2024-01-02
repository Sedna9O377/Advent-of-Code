file = open("input/day2.txt", "r")

'''
for line in file:
    game, draws = line.split(":")
    n, game = game.split(" ")
    game = int(game)            # game number
    draws = draws.split(";")    # list of draws
    for draw in draws:
        ballset = {}
        colours = draw.split(",| ")
        for i in range(0, len(colours)-1, 2):
            ballset[colours[i]] = int(ballset[colours[i + 1]])
    games[game] = ballset

print(games[3])
'''
'''
for j in range(0, len(draws_split)):
    one = draws_split[j][1:].split(" ")
    print(one)
    for i in range(0, len(one)-1, 2):
        name = one[i+1].strip(",|\n")
        balls[name] = int(one[i])
    draws.append(balls)
print(draws)
'''
result = 0

for line in file:
    game_, draws_ = line.split(":")
    n, game_ = game_.split(" ")
    game = int(game_)               # game number as int

    draws = draws_.split(";")       # a list of draws

    balls = {}
    for i in range(0, len(draws)):
        current = draws[i][1:].split(" ")
        for j in range(0, len(current)-1, 2):
            name = current[j+1].strip(",|\n")
            amount = int(current[j])
            if name in balls:
                if balls[name] < amount:
                    balls[name] = amount
            else:
                balls[name] = amount
    if balls["red"] < 13 and balls["green"] < 14 and balls["blue"] < 15:
        result += game
print(result)
