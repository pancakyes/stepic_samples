courses = {'Math': 0, 'Phisics': 0, 'Russian': 0}
students = {}
count = 0

with open('dataset_3363_4.txt', 'r') as data:
    for line in data:
        words = line.split(';')
        courses['Math'] += int(words[1])
        courses['Phisics'] += int(words[2])
        courses['Russian'] += int(words[3])
        students[words[0]] = (int(words[1]) + int(words[2]) + int(words[3]))/3
        count += 1

print(courses)
print(students)
with open('result.txt', 'w') as data2:
    for every in students:
        data2.write(str(students[every]) + '\n')
    data2.write(str(courses['Math']/count) +' ' +  str(courses['Phisics']/count) + ' ' +  str(courses['Russian']/count) + '\n')
