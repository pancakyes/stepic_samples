lst = [int(i) for i in input().split()]
x = int(input())

if x in lst:
    len_of_list = len(lst)
    for i in range(len_of_list):
        if lst[i] == x:
            print(i, end = ' ')
else:
    print('Отсутствует')

print()
