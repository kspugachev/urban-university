"""
Домашнее задание по теме "Декораторы".
"""

def is_prime(func):  # Функция декоратор.
	def wrapper(a, b, c):
		sum_three_result = func(a, b, c)

		# Кроме простых и составных чисел есть числа, не принадлежащие ни к одной из этих категорий:
		if sum_three_result < 2:
			return f'Ни простое, ни составное\n{sum_three_result}'

		# Если sum_three_result будет равен 2, то цикл for не будет реализован, так как в него будет передана пустая
		# последовательность. Следовательно, число 2 будет отнесено к простым числам:
		for i in range(2, sum_three_result):
			if sum_three_result % i == 0:
				return f'Составное\n{sum_three_result}'

		return f'Простое\n{sum_three_result}'

	return wrapper

@is_prime
def sum_three(a, b, c):  # Декорируемая функция.
	return a + b + c

result = sum_three(2, 3, 6)
print(result)
