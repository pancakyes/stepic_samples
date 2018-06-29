n = int(input())

x, y = 0, 0

for _ in range(n):
    step = input().split()
    if step[0] == 'север':
        y += int(step[1])
    elif step[0] == 'юг':
        y -= int(step[1])
    elif step[0] == 'восток':
        x += int(step[1])
    else:
        x -= int(step[1])

print (x, y)
