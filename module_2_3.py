"""
Домашняя работа по уроку "Стиль кода часть II. Цикл While".
Нужно выписывать из списка только положительные числа до тех пор, пока не встретится отрицательное или не закончится
список (выход за границу).
"""

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0  # Реализуем метод последовательного перебора значений списка.
while index < len(my_list):  # Ограничиваем цикл длиной списка, чтобы не произошла ошибка.
    if my_list[index] > 0:  # Если условие выполняется, то выводится текущий элемент списка и осуществляется переход к
        # следующему элементу.
        print(my_list[index])
        index += 1
    elif my_list[index] == 0:  # Если условие выполняется, то текущий элемент списка не выводится и осуществляется
        # переход к следующему элементу.
        index += 1
    else:
        break  # Цикл завершается, если вышеуказанные условия не реализуются.