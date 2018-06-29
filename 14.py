a = []

while True:
    current_line = input()
    if current_line == 'end':
        break
    else:
        a.append([int(i) for i in current_line.split()])

lines = len(a)
columns = len(a[0])
b = [[0 for i in range(columns)] for j in range(lines)]

for i in range(lines):
    for j in range(columns):
        b[i][j] = a[i - 1][j] + a[i][j - 1]
        if i == lines - 1:
            b[i][j] += a[0][j]
        else:
            b[i][j] += a[i + 1][j]
        if j == columns - 1:
            b[i][j] += a[i][0]
        else:
            b[i][j] += a[i][j + 1]

for i in range(lines):
    for j in range(columns):
        print(b[i][j], end = ' ')
    print()
