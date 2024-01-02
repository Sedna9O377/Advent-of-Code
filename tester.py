sequence = [10, 13, 16, 21, 30, 45]
path = [sequence]
while not all(s == 0 for s in path[-1]):
    incoming = []
    current = path[-1]
    for i in range(0, len(current) - 1):
        incoming.append(current[i + 1] - current[i])
    path.append(incoming)
    print(incoming)

result = 0
for i in range(len(path) - 2, -1, -1):
    if i % 2 == 0:
        result -= path[i][0]
    else:
        result += path[i][0]
    print(result)
