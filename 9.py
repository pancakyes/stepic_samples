my_list = [int(i) for i in input().split()]

len_of_list = len(my_list)

if len_of_list == 1:
    print(my_list[0])
else:
    for i in range(len_of_list):
        n = i - 1
        if i == len_of_list - 1:
            m = 0
        else: 
            m = i + 1 
        print(my_list[n] + my_list[m], end = ' ')
    print() 
