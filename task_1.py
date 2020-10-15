"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit
import random

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

nums = [random.randint(-100,100) for i in range(10000)]

print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))


def func_2(n):
    new_arr = [el for el in nums if el%2 == 0]
    return new_arr

n = [random.randint(-100,100) for i in range(10000)]

print(timeit.timeit("func_2(n)", setup="from __main__ import func_2, n", number=1000))

#В результате замеров выяснили, что с приминением генераторного выражения скорость увеличилась почти в 2 раза