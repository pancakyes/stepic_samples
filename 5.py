a = int(input())
b = int(input())

if a % 3 != 0:
    a = a + (3 - a % 3)

ssum = 0
numb = 0

for i in range (a, b + 1, 3):
    ssum += i
    numb += 1

print (ssum / numb)
