import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as file:
    contacts_list = list(csv.reader(file, delimiter=','))

for line in contacts_list:
    list_line = []
    for part in line[0:3]:
        if part:
            list_line.extend(part.split(' '))
    list_line = list_line + [''] * (3 - len(list_line))
    line[:3] = list_line



    final_phone = re.sub(r"(\+7|8)\W*(\d{3})\W*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})",
                         r"+7(\2)\3-\4-\5", line[5])
    phone = re.sub(r"\(*доб.\s*(\d{4})\)*", r"доб.\1", final_phone)
    line[5] = phone
print(contacts_list)

final_contacts = []
final_contacts.append(contacts_list[0])
index_list = []

for index in range(1, len(contacts_list)):
    line = contacts_list[index]

    identical_list = [n for n, j in enumerate(contacts_list) if j[:2] == line[:2]]
    list_1 = ['' for i in range(len(line))]
    for num_identical in identical_list:
        if num_identical not in index_list:

            list_2 = [(contacts_list[num_identical][i] if list_1[i] == '' else list_1[i]) for i in range(len(list_1))]
            list_1 = list_2
            index_list.append(num_identical)
    if list_1 != ['' for i in range(len(line))]:
        final_contacts.append(list_1)
print(final_contacts)


with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts)

