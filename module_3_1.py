"""
Домашняя работа по уроку "Пространство имён".
Цель: реализовать автоматический подсчет количества выполнений функций.
"""

calls = 0


def count_calls():
    global calls  # Используем глобальную переменную. При вызове текущей функции она увеличивается на 1.
    calls += 1


def string_info(string):
    count_calls()  # Помещаем count_calls() для подсчета количества выполнений данной функции.
    mod_string = (len(string), string.upper(), string.lower())
    return mod_string


def is_contains(string, list_to_search):
    count_calls()  # Помещаем count_calls() для подсчета количества выполнений данной функции.
    lower_list = [i.lower() for i in list_to_search]  # Переводим сравниваемые элементы в единый регистр.
    if string.lower() in lower_list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
