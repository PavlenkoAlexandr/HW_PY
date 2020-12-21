import re
import csv


def normalize_list(contact_list: list):

    normalized_contact_list = []
    for row in contact_list:
        pattern = re.compile(r'(\w+)\s*(\w*)\s*(\w*),(\w*) *(\w*),(\w*),(\w*),([^,]*),(.*),(.*)')
        row = pattern.sub(r'\1,\2\4,\3\5\6,\7,\8,\9,\10', ','.join(row)).split(',')
        normalized_contact_list.append(row)
    return normalized_contact_list


def combine_duplicate(lst: list):

    pairs = {}
    for item in lst:
        if item[0] in pairs:
            pairs[item[0]][0] = item[0] if item[0] else pairs[item[0]][0]
            pairs[item[0]][1] = item[1] if item[1] else pairs[item[0]][1]
            pairs[item[0]][2] = item[2] if item[2] else pairs[item[0]][2]
            pairs[item[0]][3] = item[3] if item[3] else pairs[item[0]][3]
            pairs[item[0]][4] = item[4] if item[4] else pairs[item[0]][4]
            pairs[item[0]][5] = item[5] if item[5] else pairs[item[0]][5]
            pairs[item[0]][6] = item[6] if item[6] else pairs[item[0]][6]
        else:
            pairs[item[0]] = item
    return list(pairs.values())


def normalize_numbers(lst: list):

    normalized_list = []
    for item in lst:
        pattern = re.compile(r'(\+7|8)?\s*\(*(\d{3})\)*\s*-*(\d{3})\s*-*(\d{2})\s*-*(\d{2})\s*\(*(доб\.\s*(\d{4})\)*)*')
        item = ','.join(item)
        if 'доб.' in item:
            item = pattern.sub(r'+7(\2)\3-\4-\5 доб.\7', item).split(',')
        else:
            item = pattern.sub(r'+7(\2)\3-\4-\5', item).split(',')
        normalized_list.append(item)
    return normalized_list


if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    contacts_list = normalize_numbers(combine_duplicate(normalize_list(contacts_list)))

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
