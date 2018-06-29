i = 0
s = 0
while i < 10:
    print(i,s)
    i = i + 1
    print('i = {}'.format(i))
    s = s + i
    print('s = {}'.format(s))
    if s > 15:
        break
    i = i + 1
    print('i = {}'.format(i))

print(i)
