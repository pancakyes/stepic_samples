import requests

with open('dataset_3378_3.txt', 'r') as first_file:
    url = first_file.read()
    url = url.strip()

#check = ''
while True:
    current_file = requests.get(url)
    file_data = current_file.text
    if file_data[:2] == 'We':
        break
    else:
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + file_data
    print(url)

print(file_data)
