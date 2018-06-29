a = int(input())
b = int(input())

def delitel(a, b):
    counter = 2
    all_mn = []
    while a > 1 and b > 1:
        if a % counter == 0 and b % counter == 0:
            all_mn.append(counter)
            a = a // counter
            b = b // counter
        elif a % counter == 0:
            all_mn.append(counter)
            a = a // counter
        elif b % counter == 0:
            all_mn.append(counter)
            b = b // counter
        else:
            counter += 1
    all_mn.append(max(a,b))
    return all_mn

all_mn = delitel(a, b)

result = 1

for every in all_mn:
    result *= every

print(result)
