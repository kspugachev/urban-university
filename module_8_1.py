"""
Домашнее задание по теме "Try и Except".
"""

def add_everything_up(a, b):
	try:
		return f'Все прошло без ошибок: {round(a + b, 3)}'
	except TypeError as exc:
		return f'Несмотря на эту ошибку ({exc}), программисты добьются своего: {str(a) + str(b)}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
