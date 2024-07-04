# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# Проверка на равенство типов самолетов (операция = =);
# Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# Сравнение двух самолетов по максимально возможному количеству пассажиров на
# борту (операции > < <= >=).

class Airplane:
    def __init__(self, type, capacity):
        self.type = type
        self.capacity = capacity

    def __eq__(self, other):
        if self.type == other.type:
            return True
        return False
    
    def __add__(self, passengers):
        return Airplane(self.type, self.capacity + passengers)
    
    def __sub__(self, passengers):
        return Airplane(self.type, self.capacity - passengers)
    
    def __iadd__(self, other):
        self.capacity += other.capacity
        return self
    
    def __isub__(self, other):
        self.capacity -= other.capacity
        return self
    
    def __gt__(self, other):
        if self.capacity > other.capacity:
            return True
        return False
    
    def __lt__(self, other):
        if self.capacity < other.capacity:
            return True
        return False
    
    def __ge__(self, other):
        if self.capacity >= other.capacity:
            return True
        return False
    
    def __le__(self, other):
        if self.capacity <= other.capacity:
            return True
        return False
    
    
Boeing747 = Airplane('civilian', 100)
B52_Stratofortress = Airplane('military', 30)

print(Boeing747 == B52_Stratofortress)

Boeing777 = Boeing747 + 100
print(Boeing777.capacity)
B2_Spirit = B52_Stratofortress - 10
print(B2_Spirit.capacity)

print(Boeing747 > Boeing777)
print(B52_Stratofortress < B2_Spirit)
print(Boeing747 >= B52_Stratofortress)
print(B2_Spirit <= Boeing777)