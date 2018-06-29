import operator

all_words = {}
with open ('dataset_3363_3.txt', 'r') as data:
    for line in data:
        for word in line.split():
            word = word.lower()
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1

res = max(all_words.items(), key=operator.itemgetter(1))[0]
#print(res, all_words[res])

with open ('result.txt', 'w') as data2:
    data2.write(res + ' ' + str(all_words[res]))
