"""
Домашняя работа по уроку "Модули и пакеты".
Цель: создать модули fake_math и true_math в которых будут функции отвечающие за деление, но разными способами.
Импортировать в module_4_1 функции из модулей fake_math и true_math.
"""

from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
