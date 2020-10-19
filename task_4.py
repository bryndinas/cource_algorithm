"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
import time

start_time = time.time()
sample_dict = {a: a * a for a in range(500000)}
end_time = time.time()
print(end_time-start_time)


start_time = time.time()
ordered_dict = collections.OrderedDict({a: a * a for a in range(500000)})
end_time = time.time()
print(end_time-start_time)

""" По результатам замеров можно сделать вывод о том, что обычные словари работают быстрее"""