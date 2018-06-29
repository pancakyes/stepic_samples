
newline = ''
group_chars = ''
with open('dataset_3363_2.txt', 'r') as data:
    line = data.readline()
    for char in line:
        if char.isdigit():
            group_chars += char
        elif group_chars == '':
            group_chars += char
        else:
            newline += group_chars[0] * int(group_chars[1:])
            group_chars = char

with open('result.txt', 'w') as result:
    result.write(newline)
