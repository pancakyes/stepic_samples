classes = {}

for class_number in range(11):
    classes[class_number + 1] = [0, 0]

with open ('dataset_3380_5.txt', 'r') as all_data:
    for line in all_data:
        data = line.split('\t')
        data[0] = int(data[0])
        data[2] = int(data[2])
        classes[data[0]][0] += int(data[2])
        classes[data[0]][1] += 1

for every in range(1,12):
    if classes[every][1] == 0:
        print(every, '-')
    else:
        print(every, classes[every][0] / classes[every][1])
