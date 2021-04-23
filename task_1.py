"""
Петя очень любит наблюдать за электронными часами. Он целыми днями смотрел на часы и считал, чсколько раз встречается
каждая цифра. Через несколько месяцев он научился по любому промежутку времени говорить, сколько раз на часах за это
время встретится каждая цифра, и очень гордился этим.
Вася решил проверит Петю, но он не знает, как это сделать. Вася попросил Вас помочь ему. Напишите программу, решающую
эту задачу.
"""


def sec_time_parser(param, param_1):
    """
    Функция конвертирует начальное и конечное время из формата часы:минуты:секунды в формат секунды:секунды:секунды
    :param param: list
    :param param_1: list
    :return: list, list
    """
    sec_start_parser = []
    sec_end_parser = []
    sec = 3600
    for i in range(3):
        sec_start_parser.append(param[i] * sec)
        sec_end_parser.append(param_1[i] * sec)
        sec /= 60
    return sec_start_parser, sec_end_parser


def time_counter(param, param_1):
    """
    Функция формирует список из времен, возникающих на дисплее электронных часов от начального времени до конечного с
    интервалом в секунду
    :param param: list
    :param param_1: list
    :return: list
    """
    storage = []
    while param != param_1:
        storage.extend(param)
        param[2] += 1
        if param[2] > 59:
            param[1] += 1
            param[2] = 0
        if param[1] > 59:
            param[0] += 1
            param[1] = 0
    else:
        storage.extend(param)
        return storage


def str_parser(param):
    """
    Функция преобразует список чисел в список строк, дополняя их ведущими нулями до второго разряда
    :param param: list
    :return: list
    """
    param = [str(i).zfill(2) for i in param]
    param = ''.join(map(str, param))
    return param


def digit_counter(param):
    """
    Функция возвращает словарь формата 'цифра': кол-во повторений этой цифры в списке param
    :param param: list
    :return: dict
    """
    digit_separator = {
        '0': param.count('0'),
        '1': param.count('1'),
        '2': param.count('2'),
        '3': param.count('3'),
        '4': param.count('4'),
        '5': param.count('5'),
        '6': param.count('6'),
        '7': param.count('7'),
        '8': param.count('8'),
        '9': param.count('9')
    }
    return digit_separator


# тело программы
start_time = input('Начальное время в формате hh:mm:ss - ')
end_time = input('Конечное время в формате hh:mm:ss - ')

start_parser = [int(i) for i in start_time.split(':')]
end_parser = [int(i) for i in end_time.split(':')]

result = sec_time_parser(start_parser, end_parser)

if sum(result[0]) > sum(result[1]):
    print('error')
else:
    digits = str_parser(time_counter(start_parser, end_parser))
    result = digit_counter(digits)
    for key, value in result.items():
        print(f'Число {key} - встречается {value} раз')
