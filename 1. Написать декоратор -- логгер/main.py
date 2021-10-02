from datetime import datetime


def write_logging(function):
    def write(*args, **kwargs):
        with open('def_logging.log', 'a', encoding='utf-8') as log_file:
            result = function(*args, **kwargs)
            log_file.write(f'Дата и время вызова функции: {datetime.now()}\n'
                           f'Имя функции: {function.__name__}\n'
                           f'Аргументы, с которыми вызвалась ф-ия: {args, kwargs}\n'
                           f'Возвращаемое значение функции: {result}\n\n\n')
        return result
    return write


@write_logging
def find_a_unique_id(ids_dict):
    geo_ids = ids_dict.values()
    all_ids = []
    for id in geo_ids:
        all_ids += id
    res = list(set(all_ids))
    return res


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}






print(find_a_unique_id(ids))





















# def counting_expenses():
#     salary = int(input('Введите заработную плату в месяц: '))
#     interest_mortgage = int(input('Введите, какой процент(%) уходит на ипотеку: '))
#     interest_on_life = int(input('Введите, какой процент(%) уходит на жизнь: '))
#
#     return f'\nВывод: \nНа ипотеку было потрачено: {(salary / 100) * interest_mortgage * 12}' \
#            f'\nБыло накоплено: {(100 - (interest_mortgage + interest_on_life)) * (salary / 100) * 12}'
#
# print(counting_expenses())