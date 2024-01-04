

file = open("input/day2.txt", "r")

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

file.close()


# part 2

file = open("input/day2.txt", "r")

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
    power = 1
    power *= balls["red"]
    power *= balls["green"]
    power *= balls["blue"]
    result += power
print(result)

file.close()
