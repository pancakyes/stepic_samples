s = [int(i) for i in input().split()]

s.sort()
elem = s[0]
count = 0

for i in s:
    if i == elem:
        count += 1
    else:
        if count > 1:
            print (elem, end = ' ')
        count = 1
        elem = i
if count > 1:
    print (elem, end = ' ')
print()
