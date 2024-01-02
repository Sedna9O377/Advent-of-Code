

suma = 0

file = open("input/day9.txt", "r")


for line in file:
    sequence = [int(n) for n in line.split()]
    path = [sequence]
    while not all(s == 0 for s in path[-1]):
        incoming = []
        current = path[-1]
        for i in range(0, len(current) - 1):
            incoming.append(current[i + 1] - current[i])
        path.append(incoming)

    result = 0
    for i in range(len(path) - 2, -1, -1):
        result -= path[i][0]
    suma += result
print(suma)
