# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных
# операторов:
# Проверка на равенство радиусов двух окружностей (операция = =);
# Сравнения длин двух окружностей (операции >, <, <=,>=);
# Пропорциональное изменение размеров окружности, путем изменения ее радиуса
# (операции + - += -=).

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    # метод для вычисления длины окружности
    def length(self):
        length = 2 * 3.14 * self.radius
        return length

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        return False
    
    def __gt__(self, other):
        if self.length() > other.length():
            return True
        return False
    
    def __lt__(self, other):
        if self.length() < other.length():
            return True
        return False
    
    def __ge__(self, other):
        if self.length() >= other.length():
            return True
        return False
    
    def __le__(self, other):
        if self.length() <= other.length():
            return True
        return False
    
    # Как я понял здесь разница между +,- и +=,-= состоит в том, что в первых случаях нужно создавать НОВЫЙ объект класса
    # с таким радиусом, который будет на основе радиуса из другого объекта класса, но увеличенным или уменьшенным на 
    # какое-то значение.. 
    def __add__(self, value):
        return Circle(self.radius + value)
    
    def __sub__(self, value):
        return Circle(self.radius - value)
    
    # а во вторых случаях будет изменяться (перезаписываться) радиус объекта, увеличившись или уменьшившись на радиус 
    # из другого объекта
    def __iadd__(self, other):
        self.radius += other.radius
        return self
    
    def __isub__(self, other):
        self.radius -= other.radius
        return self

    
circle1 = Circle(5)
circle2 = Circle(10)

# Сравниваем радиусы окружностей
print(circle1 == circle2)
# Сравниваем длины окружностей
print(circle1 > circle2)
print(circle1 < circle2)
print(circle1 >= circle2)
print(circle1 <= circle2)
# Создаем новые объекты класса со своими радиусами
circle3 = circle1 + 15
print(circle3.radius)
circle4 = circle2 - 3
print(circle4.radius)
# Изменяем радиусы уже существующих объектов
circle1 += circle3
print(circle1.radius)
circle2 -= circle4
print(circle2.radius)