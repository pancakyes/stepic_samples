objects = [1, 2, 1, 2, 3]

set_of_ids = set()
for obj in objects:
    set_of_ids.add(id(obj))

print(len(set_of_ids))
