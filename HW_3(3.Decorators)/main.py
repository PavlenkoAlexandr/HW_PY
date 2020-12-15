from datetime import datetime
from typing import Callable
from superheroapi import find_hero
import os


def log_path_decor(path: str):
    def log_decor(old_func: Callable):
        def new_func(*args, **kwargs):
            with open(os.path.join(path, 'log.txt'), 'w', encoding='utf-8') as f:
                f.write(
                    f'{datetime.now()}\n'
                    f'Выполнена функция {old_func.__name__} с аргументами {args, kwargs}\n'
                    f'Результат выполнения функции:\n{old_func(*args, **kwargs)}'
                )
            return old_func(*args, **kwargs)
        return new_func
    return log_decor


if __name__ == '__main__':

    path_maker = log_path_decor(os.getcwd())
    log = path_maker(find_hero)
    log('Thanos', 'thanos')
