"""
Дополнительное практическое задание по модулю: "Наследование классов".
"""

from math import pi


class Figure:
    sides_count = 0

    # При создании объектов делаем проверку на количество переданных сторон. Если сторон не ровно sides_count, то
    # создаем массив с единичными сторонами и в том кол-ве, которое требует фигура.
    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        self.__sides = sides if len(sides)==self.sides_count else [1]*self.sides_count

    def get_color(self):
        """
        Возвращает список RGB цветов.
        """
        return list(self.__color)

    @staticmethod
    def __is_valid_color(r, g, b):
        """
        Проверяет корректность переданных значений перед установкой нового цвета.
        """
        a = []
        if 0 <= r <= 255 and isinstance(r, int):
            a.append(True)
        else:
            a.append(False)
        if 0 <= g <= 255 and isinstance(g, int):
            a.append(True)
        else:
            a.append(False)
        if 0 <= b <= 255 and isinstance(b, int):
            a.append(True)
        else:
            a.append(False)
        if all(a):
            return True

    def set_color(self, r, g, b):
        """
        Принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно
        проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        """
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        """
        Принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во
        новых сторон совпадает с текущим, False - во всех остальных случаях.
        """
        b = []
        for i in sides:
            if isinstance(i, int) and i > 0:
                b.append(i)

        if len(b) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        """
        Возвращает значения атрибута __sides.
        """
        return list(self.__sides)

    def __len__(self):
        """
        Возвращает периметр фигуры.
        """
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """
        Принимает новые стороны. Если их количество не равно sides_count, то не изменяет. В противном случае - изменяет.
        """
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.radius = self.radius(sides)

    @staticmethod
    def radius(length):
        """
        Рассчитывает радиус исходя из длины окружности.
        """
        return length / (2*pi)

    def get_square(self):
        """
        Возвращает площадь круга.
        """
        return pi*(self.__radius)**2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        """
        Возвращает площадь треугольника.
        """
        p = sum(self._Figure__sides) / 2
        #a, b, c = self.__sides
        return (p * (p - self.__sides[1]) *
                (p - self.__sides[2]) *
                (p - self.__sides[3])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        sides = [side] * 12  # Переопределяем __sides, сделав список из 12 одинаковы сторон.
        super().__init__(color, *sides)

    def get_volume(self):
        """
        Возвращает объём куба.
        """
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
