import json
import hashlib


class Urlmaker:

    def __init__(self, file):
        with open(file, encoding='utf-8') as f:
            self.data = json.load(f)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.data):
            raise StopIteration
        return self.data[self.cursor]['name']['common']


def text_to_hash(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()


if __name__ == '__main__':

    countries = Urlmaker('countries.json')
    with open('result.txt', 'w', encoding='utf-8') as f:
        for country in countries:
            f.write(f'{country} - https://en.wikipedia.org/wiki/{country.replace(" ", "_")} \n')

    for line in text_to_hash('result.txt'):
        print(hashlib.md5(line.encode('utf-8')).hexdigest())
