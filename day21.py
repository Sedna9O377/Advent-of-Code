
LINE_LENGTH = 131
S_LOCATION = 65

file = (open('input.txt', 'r'))
content = file.readlines()

start = [[S_LOCATION, S_LOCATION]]
positions = set(tuple(i) for i in start)
positions2 = set()
final = set()


def step(x, y):
    t = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
    for i in t:
        line = content[i[0]]
        if line[i[1]] != '#':
            positions2.add(tuple(i))


for i in range(63):
    for p in positions:
        step(p[0], p[1])
    positions = positions2
    positions2 = set()
    for i in positions:
        final.add(i)


print(len(final))

file.cc