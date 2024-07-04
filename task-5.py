# Создайте класс Roman (РимскоеЧисло), представляющий римское число и
# поддерживающий операции +, -, *, /.
# При реализации класса:
# операции +, -, *, / реализуйте как специальные методы
# методы преобразования как статические методы

class Roman:
    def __init__(self, roman_number):
        self.roman_number = roman_number

    # Создадим статистический метод, который будет принимать римское число как строку и выдавать его числовой эквивалент
    @staticmethod
    def roman_to_int(roman): # здесь нет self потому что статистическому методу не нужно работать с экземпляром класса,
                             # да и со всем классом в целом
        # создадим словарь, где каждому римскому числу соответствует его число
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int = 0
        # пройдемся по каждому символу принятого римского числа по всей его длине по индексам 
        for i in range(len(roman)):
            if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i - 1]]: # здесь устанавлием гарантию того, что мы не
                                                                          # не выйдем за пределы длины строки i > 0, 
                                                                          # и проверяем, больше ли текущее значение 
                                                                          # римского числа предыдущего, Например, 
                                                                          # в числе IV (4), V (5) больше, чем I (1).
            # Эта проверка нам нужна для таких случаев, когда в римском числе меньший элемент стоит перед большим.
            # Например число "IV" I это 1, V это 5, 1 < 5, но числовой эквивалент его это 4. 
            # Чтобы получить в итоге 4 нам нужно из большего элемента отнять удвоенное значение предыдущего элемента и 
            # прибавить все это к меньшему элементу.
            # 4 = 1(меньший элемент) + (5(больший элемент) - 2 * 1(меньший элемент)) = 1 + (5 - 2 * 1) = 1 + 3 = 4                                                            
                int += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
            else: # если же не выполняется условие, то тогда просто добавляем значение элемента к общему числу
                int += roman_dict[roman[i]]
        return int
    
    # Разберем все на конкретном примере. Допустим roman = 'XIV'
    # int = 0
    # Запускаем цикл:
        # 1) i = 0, roman[0] = 'X' - первый элемент строки roman, int = 0
           # i > 0 and roman_dict[roman[0]] > roman_dict[roman[0-1]] - не выполняется
           # int += roman_dict['X'] - обращаемся к значению словаря по его ключу
           # int = 0 + 10 = 10
        # 2) i = 1, roman[1] = 'I' - второй элемент строки roman, int = 10
           # i > 0 and roman_dict[roman[1]] > roman_dict[roman[1-1]]
           # i > 0 and roman_dict['I'] > roman_dict[roman[0]]
           # i > 0 and 1 > roman_dict['X']
           # i > 0 and 1 > 10 - не выполняется
           # int += roman_dict['I'] - обращаемся к значению словаря по его ключу
           # int = 10 + 1 = 11
        # 3) i = 2, roman[2] = 'V' - третий элемент строки roman, int = 11
           # i > 0 and roman_dict[roman[2]] > roman_dict[roman[2-1]]
           # i > 0 and roman_dict['V'] > roman_dict['I']
           # i > 0 and 5 > 1 - выполняется условие
           # int += roman_dict[roman[2]] - 2 * roman_dict[roman[2 - 1]]
           # int += roman_dict['V'] - 2 * roman_dict[roman['I']]
           # int += 5 - 2 * 1
           # int += 3
           # int = 11 + 3 = 14     return int = 14

    # Теперь создадим метод, выполняющий обратную функцию, то преобразует обычное число в римское       
    @staticmethod
    def int_to_roman(int):
        # Создадим два списка, первый из которых будет хранить обычные числа..
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # а второй - и их эквиваленты в римских цифрах
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # Используем списки, а не словарь, потому что нам здесь важна упорядоченность, для римских цифр она играет
        # очень важную роль, потому что там всегда первым пишется символ с большим значением и далее по уменьшению.
        # Также здесь добавляем сокращения для таких случаев, когда символ с меньшим значением стоит перед символом
        # с большим, например "СD" C - 100, D - 500, CD - 400, без сокращения это бы писалось как "CCCC".
        # В предыдущем методе это решалось за счет условия, но здесь эти сокращения необходимо учесть.

        # Создадим переменную для хранения римского числа
        roman_number = ''
        # и специальную переменную для итерации по спискам val и syb
        i = 0
        # Создаем цикл, который будет выполняться пока принятое число int > 0
        while int > 0:
            # Создаем вложенный цикл, который будет определять, сколько раз текущий элемент из val помещается в оставшееся
            # значение int
            for _ in range(int // val[i]): # '_' это не используемая переменная, с помощью которой мы будем проводим 
                                           # итерации. В range у нас будет помещаться число, получаемое в результате
                                           # целочисленного деления принимаемого числа int на элемент из списка val 
                                           # под индексом i. 
                roman_number += syb[i]     # Затем будем брать элемент из списка syb под индеском i и добавлять  
                                           # (конкатенировать) ее в переменную roman_number
                int -= val[i]              # После этого число int уменьшаем на значение из списка val под индексом i
                                           # и итерация цикла for завершается  
            # Далее в цикле while увеличиваем число i на 1         
            i += 1 
        return roman_number
        
    # Разберем все на примере. Допустим int = 1987
    # roman_number = ''
    # i = 0
    # запускаем цикл while, int = 1987 > 0
    #   1) запускаем цикл for, int // val[0] = 1987 // 1000 = 1
         # for _ in range(1): - будет одна итерация
            # 1.1) roman_number = '' + syb[0] = '' + 'M' = 'M'
                 # int = 1987 - val[0] = 1987 - 1000 = 987
         # i = 0 + 1 = 1
    # int = 987 > 0
    #   2) запускаем цикл for, int // val[1] = 987 // 900 = 1
         # for _ in range(1):
            # 2.1) roman_number = 'M' + syb[1] = 'M' + 'CM' = 'MCM'
                 # int = 1987 - val[1] = 987 - 900 = 87
         # i = 1 + 1 = 2
    # int = 87 > 0
    #   3) запускаем цикл for, int // val[2] = 87 // 500 = 0 ни одного целого значения из var не помещается в int, это
         # for _ in range(0) означает что диапазон отсутствует, а значит цикл for не запустится
         # i = 2 + 1 = 3
    # int = 87 > 0
    #   4) запускаем цикл for, int // val[3] = 87 // 400 = 0
         # for _ in range(0)  for не запускается
         # i = 3 + 1 = 4
    # int = 87 > 0
    #   5) запускаем цикл for, int // val[4] = 87 // 100 = 0
         # for _ in range(0)  for не запускается
         # i = 4 + 1 = 5
    # int = 87 > 0
    #   6) запускаем цикл for, int // val[5] = 87 // 90 = 0
         # for _ in range(0)  for не запускается
         # i = 5 + 1 = 6
    # int = 87 > 0
    #   7) запускаем цикл for, int // val[6] = 87 // 50 = 1
         # for _ in range(1):
            # 7.1) roman_number = 'MCM' + syb[6] = 'MCM' + 'L' = 'MCML'
                 # int = 1987 - val[6] = 87 - 50 = 37
         # i = 6 + 1 = 7
    # int = 37 > 0
    #   8) запускаем цикл for, int // val[7] = 37 // 40 = 0
         # for _ in range(0)  for не запускается
         # i = 7 + 1 = 8
    # int = 37 > 0
    #   9) запускаем цикл for, int // val[8] = 37 // 10 = 3
         # for _ in range(3): - делаем 3 итерации, 3 значения из val помещается в int
            # 9.1) roman_number = 'MCML' + syb[8] = 'MCML' + 'X' = 'MCMLX'
                 # int = 37 - val[8] = 37 - 10 = 27 
            # 9.2) roman_number = 'MCMLX' + syb[8] = 'MCMLX' + 'X' = 'MCMLXX'
                 # int = 27 - val[8] = 27 - 10 = 17 
            # 9.3) roman_number = 'MCMLXX' + syb[8] = 'MCMLXX' + 'X' = 'MCMLXXX'
                 # int = 27 - val[8] = 17 - 10 = 7
         # i = 8 + 1 = 9
    # int = 7 > 0
    #   10) запускаем цикл for, int // val[9] = 7 // 9 = 0
         #  for _ in range(0)  for не запускается            
         #  i = 9 + 1 = 10
    # int = 7 > 0
    #   11) запускаем цикл for, int // val[10] = 7 // 5 = 1
         #  for _ in range(1):
            # 11.1) roman_number = 'MCMLXXX' + syb[10] = 'MCMLXXX' + 'V' = 'MCMLXXXV'
                 #  int = 7 - val[10] = 7 - 5 = 2            
         #  i = 10 + 1 = 11
    # int = 2 > 0
    #   12) запускаем цикл for, int // val[11] = 2 // 4 = 0
         #  for _ in range(0)  for не запускается            
         #  i = 11 + 1 = 12
    # int = 2 > 0
    #   13) запускаем цикл for, int // val[12] = 2 // 1 = 2
         #  for _ in range(2):
            # 13.1) roman_number = 'MCMLXXXV' + syb[12] = 'MCMLXXXV' + 'I' = 'MCMLXXXVI'
                 #  int = 2 - val[12] = 2 - 1 = 1             
            # 13.2) roman_number = 'MCMLXXXVI' + syb[12] = 'MCMLXXXVI' + 'I' = 'MCMLXXXVII'
                 #  int = 2 - val[12] = 1 - 1 = 0             
         #  i = 12 + 1 = 13
    # int = 0 != 0 условие while не выполняется из цикл завершается
    # return roman_number = 'MCMLXXXVII'

    # Теперь создадим дандер-методы арифметических операций для римских цифр. В них просто будут приниматься два объекта
    # класса Roman как self и other, к записанному в них атрибуту roman_number будет применяться метод roman_to_int для
    # преобразования в обычное число и далее производиться обычная арифметическая операция. Результат вычисления будет 
    # сохраняться в переменную result как число. Затем создадится новый объект класса Roman, атрибутом которого будет
    # результат выполнения метода int_to_roman с переменной result, то есть преобразования обычного числа в римское.  

    def __add__(self, other):
        result = self.roman_to_int(self.roman_number) + self.roman_to_int(other.roman_number)
        return Roman(self.int_to_roman(result))

    def __sub__(self, other):
        result = self.roman_to_int(self.roman_number) - self.roman_to_int(other.roman_number)
        return Roman(self.int_to_roman(result))

    def __mul__(self, other):
        result = self.roman_to_int(self.roman_number) * self.roman_to_int(other.roman_number)
        return Roman(self.int_to_roman(result))

    def __truediv__(self, other):
        result = self.roman_to_int(self.roman_number) // self.roman_to_int(other.roman_number)
        return Roman(self.int_to_roman(result))


roman1 = Roman('XIV')
roman2 = Roman('III')

result_add = roman1 + roman2
print(result_add.roman_number)  

result_sub = roman1 - roman2
print(result_sub.roman_number)  

result_mul = roman1 * roman2
print(result_mul.roman_number)

result_div = roman1 / roman2
print(result_div.roman_number)                       