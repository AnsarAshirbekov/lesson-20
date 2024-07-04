# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# Проверка на равенство площадей квартир (операция ==);
# Проверка на неравенство площадей квартир (операция !=);
# Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if self.area == other.area:
            return True
        return False
    
    def __ne__(self, other):
        if self.area != other.area:
            return True
        return False
    
    def __gt__(self, other):
        if self.price > other.price:
            return True
        return False
    
    def __lt__(self, other):
        if self.price < other.price:
            return True
        return False
    
    def __ge__(self, other):
        if self.price >= other.price:
            return True
        return False
    
    def __le__(self, other):
        if self.price <= other.price:
            return True
        return False
    

my_flat = Flat(50, 1000000)
your_flat = Flat(70, 2000000)

print(my_flat == your_flat)
print(my_flat != your_flat)
print(my_flat > your_flat)
print(my_flat < your_flat)
print(my_flat >= your_flat)
print(my_flat <= your_flat)