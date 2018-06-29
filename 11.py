my_list = []
summ = 0

while True:
    a = int(input())
    summ += a
    my_list.append(a)
    if summ == 0:
        break

print(sum([i * i for i in my_list]))
