n = int(input())

full_list = []
for i in range(n):
    full_list += [i + 1] * (i + 1)

for i in range(n):
    print(full_list[i], end = ' ')

print()
