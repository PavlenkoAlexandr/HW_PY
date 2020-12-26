from Stack import Stack


def is_balanced(string: str):
    open_symbols = '({['
    close_symbols = ')}]'
    symbols_pairs = {')': '(', ']': '[', '}': '{'}
    result = Stack()
    for symbol in string:
        if symbol in open_symbols:
            result.push(symbol)
        elif symbol in close_symbols:
            if result.isEmpty():
                return False
            pair = result.pop()
            if pair != symbols_pairs.get(symbol):
                return False
    return result.isEmpty()


if __name__ == '__main__':

    while True:
        string = input('\nВведите строку для проверки: ')
        print('Сбалансированно' if is_balanced(string) else 'Несбалансированно')
