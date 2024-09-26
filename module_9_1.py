"""
Домашнее задание по теме "Введение в функциональное программирование".
Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.
"""

def apply_all_func(int_list, *functions):
	result = {}
	for function in functions:
		func_result = function(int_list)
		result[function.__name__] = func_result
	return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
