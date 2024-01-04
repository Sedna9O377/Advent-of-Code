import re

suma = 0

with open("input (1).txt") as file:
    for line in file:
        start = line.index(":")
        line = line[start+2:]
        winning, num = line.split(" | ")
        if winning[0] == ' ':
            winning = winning[1:]
        if num[0] == ' ':
            num = num[1:]
        winning_num = re.split(r'\s+', winning)
        my_num = re.split(r'\s+', (num.strip("\n")))
        common = len(list(set(my_num).intersection(winning_num)))

        result = 0
        if common > 0:
            result = 1
            common -= 1
        while common > 0:
            result *= 2
            common -= 1
        suma += result

file.close()
print(suma)


# part 2

file = open("input (1).txt", "r")

cards = file.readlines()
LAST_CARD = 187


amounts = {}
for i in range(0, LAST_CARD):
    amounts[i] = 1

for i in range (0, LAST_CARD):
    start = cards[i].index(":")
    cards[i] = cards[i][start + 2:]
    winning, num = cards[i].split(" | ")
    if winning[0] == ' ':
        winning = winning[1:]
    if num[0] == ' ':
        num = num[1:]

    winning_num = re.split(r'\s+', winning)
    my_num = re.split(r'\s+', (num.strip("\n")))

    common = len(list(set(my_num).intersection(winning_num)))

    k = i
    for j in range(0, common):
        amounts[k+1] = amounts[k+1] + amounts[i]
        k += 1

result = 0
for amount in amounts.values():
    result += amount
print(result)

file.close()
