def modify_list(l):
    counter = len(l)
    while counter > 0:
        elem = l.pop(0)
        if elem % 2 == 0:
            l.append(elem // 2)
        counter -= 1




lst = [1, 2, 3, 4, 5, 6]
#print(modify_list(lst))
modify_list(lst)
print(lst)
