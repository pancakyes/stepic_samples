s = "acggtgttat"

s = input()
s = s.lower()

print(((s.count('c') + s.count('g'))/len(s)) * 100)

