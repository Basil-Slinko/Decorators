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
