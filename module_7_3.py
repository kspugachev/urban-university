"""
Домашнее задание по теме "Оператор 'with'".
"""


class WordsFinder:
	def __init__(self, *file_names):
		self.file_names = file_names

	def get_all_words(self):
		"""
		Подготовительный метод, который возвращает словарь следующего вида:
		{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
		"""
		all_words = {}

		for file_name in self.file_names:
			with open(file_name, 'r', encoding='utf-8') as file:
				file_text = file.read()
				for_replace = {',': ' ', '.': ' ', '=': ' ', '!': ' ', '?': ' ', ';': ' ', ':': ' ', ' - ': ' '}

				for old, new in for_replace.items():
					file_text = file_text.replace(old, new)

				all_words[file_name] = file_text.lower().split()
		return all_words

	def find(self, word):
		"""
		Возвращает словарь, где ключ - название файла, значение - позиция первого слова (word) в списке слов файла.
		"""
		answer = {}

		for file_key, file_list in self.get_all_words().items():
			for file_word in file_list:
				if file_word == word.lower():
					answer[file_key] = file_list.index(file_word) + 1

		return answer

	def count(self, word):
		"""
		Возвращает словарь, где ключ - название файла, значение - количество слов (word) в списке слов файла.
		"""
		answer = {}

		for file_key, file_list in self.get_all_words().items():
			answer[file_key] = file_list.count(word.lower())

		return answer


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
