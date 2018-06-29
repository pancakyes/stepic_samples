import requests

with open('dataset_3378_2.txt', 'r') as data_file:
    url = data_file.read()
    url = url.strip()

#print(url)

needed_file = requests.get(url)
#print(needed_file.text)

number_of_lines = len((needed_file.text).splitlines())
print(number_of_lines)
