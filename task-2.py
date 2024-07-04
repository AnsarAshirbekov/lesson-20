# Создайте класс Complex (комплексное число).
# Создайте перегруженные операторы для реализации арифметических операций для по
# работе с комплексными числами (операции +, -, *, /).

class Complex:
    # Комплексное число состоит из действительной и мнимой частей
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # создается новый объект класса (новое комплексное число), значение которого будет результатом сложения двух 
        # других объектов класса self и other (других комплексных чисел)
        # Действительные и мнимые части двух коплексных чисел складываются друг с другом по отдельности
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # Действительные и мнимые части двух коплексных чисел отнимаются, от первого второе, по отдельности
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # (a+bi) × (c+di) = (ac−bd)+(ad+bc)i - формула умножения комплексных чисел, где
        # a = self.real
        # b = self.imag
        # c = other.real
        # d = other.imag
        # i = просто указатель мнимой части
        # real_part = (ac−bd)
        # imag_part = (ad+bc)i
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        # (a+bi) / (c+di) = ((ac+bd) / (c**2 + d**2)) + ((bc−ad) / (c**2 + d**2))i
        # denom = (c**2 + d**2)
        denom = other.real ** 2 + other.imag ** 2
        # real_part = ((ac+bd) / (c**2 + d**2))
        # imag_part = ((bc−ad) / (c**2 + d**2))i
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real_part, imag_part)

    # Теперь сделаем так, чтобы объекты класса Complex отображались красиво, прям как в математике, со всеми + и i,
    # и чтобы всякий раз, когда мы бы выводили объекты этого класса, они отображались определеннным здесь образом
    def __repr__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(f"c1: {c1}")
print(f"c2: {c2}")

c3 = c1 + c2
print(f"c1 + c2 = {c3}")

c4 = c1 - c2
print(f"c1 - c2 = {c4}")

c5 = c1 * c2
print(f"c1 * c2 = {c5}")

c6 = c1 / c2
print(f"c1 / c2 = {c6}")