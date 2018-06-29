line = (input().lower()).split()
d = {}

for word in line:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

for word, numb in d.items():
    print(word, numb)
