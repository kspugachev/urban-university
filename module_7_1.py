"""
Домашнее задание по теме "Режимы открытия файлов"
"""


class Product:
	def __init__(self, name, weight, category):
		self.name = str(name)
		self.weight = float(weight)
		self.category = str(category)

	def __str__(self):
		return f'{self.name}, {self.weight}, {self.category}'


class Shop:
	__file_name = 'products.txt'

	def get_products(self):
		"""
		Открываем, читаем и закрываем файл products.txt. Возвращаем список продуктов.
		"""
		file = open(self.__file_name, 'r')
		products_list = file.read()
		file.close()
		return products_list

	def add(self, *products):
		"""
		Проверяем, есть ли продукт в списке. Добавляем его в список внутри products.txt, если его там нет. В противном
		случае, выводим сообщение о том, что продукт уже есть.
        """
		for i in products:
			if str(i) not in self.get_products():
				file_1 = open(self.__file_name, 'a')
				file_1.write(f'{i}\n')
				file_1.close()
			else:
				print(f'Продукт {i} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
