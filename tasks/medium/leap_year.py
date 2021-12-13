"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Високосный год

Отредактировать функцию is_year_leap, принимающую 1 аргумент — год,
и возвращающую True, если год високосный, и False иначе.

В високосном годе 366 дней, в обычном 365.
1) Если год не делится на 4, значит он обычный.
2) Иначе надо проверить не делится ли год на 100.
3) Если не делится, значит это не столетие и можно сделать вывод,
что год високосный.
4) Если делится на 100, значит это столетие и его следует проверить
его делимость на 400.
5) Если год делится на 400, то он високосный.
6) Иначе год обычный.

Проверки можно проводить последовательно, а можно группировать через
логические операторы "И" и "ИЛИ".
Поэтому способов решения задачи может быть несколько.

ПРИМЕРЫ
--------------------------------------------------------------------------------
is_year_leap(1700) -> False
is_year_leap(1800) -> False
is_year_leap(1900) -> False
is_year_leap(2100) -> False
is_year_leap(1988) -> True
is_year_leap(1600) -> True
is_year_leap(2400) -> True
"""


def is_year_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = True
    return result


if __name__ == '__main__':
    year_val = int(input('Введите год: '))
    print(f'Тип года: {is_year_leap(year_val)}')
