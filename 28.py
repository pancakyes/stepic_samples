first_line = input()
second_line = input()

length_of_alphabet = len(first_line)

direct_code = {}
reverse_code = {}

for ind in range(length_of_alphabet):
    direct_code[first_line[ind]] = second_line[ind]
    reverse_code[second_line[ind]] = first_line[ind]

first_line = input()
second_line = input()

new_first_line = ''
new_second_line = ''

for char in first_line:
    new_first_line += direct_code[char]

for char in second_line:
    new_second_line += reverse_code[char]

print(new_first_line)
print(new_second_line)
