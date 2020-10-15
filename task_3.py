"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

#Профилировка через timeit

enter_num=5156161515
print(timeit.timeit("revers(enter_num, revers_num=0)", setup="from __main__ import revers, enter_num",number=100000))
print(timeit.timeit("revers_2(enter_num, revers_num=0)", setup="from __main__ import revers_2, enter_num",number=100000))
print(timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num",number=100000))

#Профилировка через cProfile
cProfile.run('revers(enter_num, revers_num=0)')
cProfile.run('revers_2(enter_num, revers_num=0)')
cProfile.run('revers_3(enter_num)')

"""Вывод: как показал модуль timeit функция revers_3(enter_num) самая быстрая. Через модуль сProfile
не получается определить самую быструю и самую медленную функцию из чего можно сделать вывод о том,
что замеры через моудль timeit подходит для замеров небольших функций и части кода, а модуль сProfile
предназначен для больших функций, где можно детально посмотреть отчет по ней"""









