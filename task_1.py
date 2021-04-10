'''
Петя очень любит наблюдать за электронными часами. Он целыми днями смотрел на часы и считал, чсколько раз встречается
каждая цифра. Через несколько месяцев он научился по любому промежутку времени говорить, сколько раз на часах за это
время встретится каждая цифра, и очень гордился этим.
Вася решил проверит Петю, но он не знает, как это сделать. Вася попросил Вас помочь ему. Напишите программу, решающую
эту задачу.
'''


def sec_parser(param, param_1):
    sec_start_parser = []
    sec_end_parser = []
    sec = 3600
    for i in range(3):
        sec_start_parser.append(param[i] * sec)
        sec_end_parser.append(param_1[i] * sec)
        sec /= 60
    return sec_start_parser, sec_end_parser


def counter(param, param_1):
    while param != param_1:
        print(param)
        param[2] += 1
        if param[2] > 59:
            param[1] += 1
            param[2] = 0
        if param[1] > 59:
            param[0] += 1
            param[1] = 0
    else:
        return print(param)


start_time = input('Начальное время в формате hh:mm:ss - ')
end_time = input('Конечное время в формате hh:mm:ss - ')

start_parser = [int(i) for i in start_time.split(':')]
end_parser = [int(i) for i in end_time.split(':')]

result = sec_parser(start_parser, end_parser)

if sum(result[0]) > sum(result[1]):
    print('error')
else:
    counter(start_parser, end_parser)
