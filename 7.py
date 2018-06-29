s1 = 'aaaabbcaa'
s = 'abc'

letter = s[0]
count = 0
new_s = ''

for i in s:
    if i == letter:
        count += 1
    else:
        new_s = new_s + letter + str(count)
        count = 1
        letter = i

new_s = new_s + letter + str(count)
print(new_s) 
