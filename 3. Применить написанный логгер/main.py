from datetime import datetime
import os


def logger_path(path):
    def write_logging(function):
        def write(*args, **kwargs):
            os.chdir(path)
            with open('def_logging.log', 'a', encoding='utf-8') as log_file:
                result = function(*args, **kwargs)
                log_file.write(f'Дата и время вызова функции: {datetime.now()}\n'
                               f'Имя функции: {function.__name__}\n'
                               f'Аргументы, с которыми вызвалась ф-ия: {args, kwargs}\n'
                               f'Возвращаемое значение функции: {result}\n\n\n')
            return result
        return write
    return write_logging


@logger_path(f"{os.getcwd()}/logs")
def find_a_unique_id(ids_dict):
    geo_ids = ids_dict.values()
    all_ids = []
    for id_ in geo_ids:
        all_ids += id_
    res = list(set(all_ids))
    return res


if __name__ == '__main__':
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    find_a_unique_id(ids)
