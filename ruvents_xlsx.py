"""
Тестовое задание на вакансию:
Junnior Python developer
RUVENTS
https://career.habr.com/vacancies/1000069114

Описание:

"Решать задачи можно в чем угодно.
Сложные задачи можно пропускать. Сделать не все — ок.
На выходе — ответы и исходники решения задач (файл в экселе, код на питоне, …)
Постарайтесь заметить, сколько времени у вас займет решение.
Решение нужно прислать ASAP."

"""

import pandas as pd
import math
import re
from datetime import datetime
import calendar


# читаем файл (лист с задачами) и переводим в датафрейм
df = pd.read_excel('ruvents_task_support.xlsx', sheet_name='Tasks')

# удаляем строку с заданием, чтобы не мешала
df = df.drop([0])


def find_even(df):
    """
    Считает, сколько чётных чисел в столбце num1

    :param df: датафрейм из экселя
    :return: количество чётных чисел
    """
    ds = df['num1']
    return len(ds[ds % 2 == 0])


def find_primes(df):
    """
    Считает, сколько простых чисел в столбце num2

    :param df: датафрейм с таблицей
    :return: количество простых чисел столбце num2
    """
    def is_prime(num):
        """
        Определяет, простое ли число
        :param num: число для определения
        :return: True/False
        """

        if num <= 1:
            return False
        elif num == 2:
            return True

        # определяем максимальный делитель
        max_divisor = math.floor(math.sqrt(num))
        for i in range(2, max_divisor):
            if num % i == 0:
                return False
        else:
            return True
    # берём серию из столбца num2
    ds = df['num2']
    # заменяем на True/False простые/не простые числа,
    # потом оставляем в серии только те, что True
    # и возвращаем len
    return len(ds[ds.apply(is_prime)])


def less_05_2(df):
    """
    Считает, сколько чисел меньше 0.5 в столбце num3

    :param df: датафрейм
    :return: int
    """
    # создаём серию из колонки num3
    # сразу удаляем в ней пробелы, заменяем запятую на точку и переводим во флоат
    ds = df['num3'].apply(lambda s: float(s.replace(' ', '').replace(',', '.')))

    # оставляем только то, что меньше 0.5 и возвращаем количество таких чисел
    return len(ds[ds < 0.5])



def less_05_regex(df):
    """
    Считает, сколько чисел меньше 0.5 в столбце, используя re
    :param df: датафрейм
    :return: int
    """
    ds = df['num3']
    pattern = re.compile(r"^\s*0*\s*[.,]\s*[0-4]")

    def less_then_05(s):
        return pattern.match(s) is not None

    return len(ds[ds.apply(less_then_05)])


def find_tue(df):
    """
    Считает сколько вторников в столбце data1

    :param df: датафрейм
    :return: int
    """
    # Получаем список строк из столбца date1
    to_find_tue = df['date1'].tolist()
    ds_datetime = pd.to_datetime(df['date2']).dt.dayofweek

    return sum([1 for s in to_find_tue if s[:3] == 'Tue'])


def find_tue_ds(df):
    """
    Считает сколько вторников в столбце data1

    :param df: датафрейм
    :return: int
    """
    # сохраняем датафрейм в серию, убираем пасхалку
    # (наткнулся при попытке решения через перевод даты в день недели)
    ds = df['date1'].apply(lambda s: s.replace('отметьте в решении, если вы прочитали это', ''))

    # переводим строки в формат даты
    # (берём сразу дни недели в числовом выражении, где 0 - пн, 6 - вс; нам нужен вт == 1)
    ds = pd.to_datetime(ds).dt.dayofweek

    # считаем всё, что равно единице
    return len(ds[ds == 1])


def find_tue2(df):
    """
    Считает сколько вторников в столбце data2

    пример входного формата: '2026-07-19 08:15:41.695463'

    :param df: датафрейм
    :return: int
    """
    # берём датафрейм переводим строки в формат даты и сохраняем как дата серию (тк взяли один столбец)
    # (берём сразу дни недели в числовом выражении, где 0 - пн, 6 - вс; нам нужен вт == 1)
    ds_datetime = pd.to_datetime(df['date2']).dt.dayofweek

    # считаем всё, что равно единице
    return len(ds_datetime[ds_datetime == 1])


def find_last_tue(df):
    """
    считает сколько последних вторников месяца в столбце date3

    :param df: датафрейм
    :return: int
    """

    def is_last_tue(date):
        """
        возвращает последний вторник месяца по введённой дате
        и сравнивает день даты и последний вторник

        :param date: дата
        :return: True - если это последний вторник, False - если нет
        """

        # находим последний вторник в месяце введённого года (по введённой дате)
        # используем для этого модуль calendar
        last_tue = max(week[1] for week in calendar.monthcalendar(date.year, date.month))

        # возвращаем True/False, если введённая дата - это последний вторник месяца
        return date.day == last_tue

    ds = pd.to_datetime(df['date3'])

    return len(ds.apply(is_last_tue))
