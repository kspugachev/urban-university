"""
Самостоятельная работа по уроку "Произвольное число параметров".
Цель: написать функцию, которая принимает одно обязательное слово и неограниченную последовательность.
Функция должна составить новый список только из тех слов неограниченной последовательности, которые содержат
обязательное слово или наоборот.
"""


def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():  # Ищем обязательное слово в неограниченной последовательности.
            same_words.append(i)
        elif i.lower() in root_word.lower():  # Ищем слова из неограниченной последовательности в обязательном слове.
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
