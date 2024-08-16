"""
Домашняя работа по уроку "Пространство имен".
"""

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
#inner_function()  # We can't call a function in the global space from the local space of another function.
