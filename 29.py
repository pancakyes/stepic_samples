d = int(input())

dictionary = []

for _ in range(d):
    word = input()
    dictionary.append(word.lower())

errors = set()

l = int(input())
for _ in range(l):
    line = input().split()
    for word in line:
        if word.lower() not in dictionary:
            errors.add(word)

for word in errors:
    print(word)

