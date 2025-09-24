# Задача 2. Калькулятор
# Составьте программу, которая запрашивает у пользователя 2 целых числа и выполняет операции:
# ●	арифметические: +, -, * , / , // , %, **, log10;
# ●	сравнение: <, <=, >, >=, !=, ==,
# выводя на экран результат каждого действия. 
# В случае получение вещественного результата, округлите его до 
# 2-х знаков после запятой (используя функцию round()).
# Подсказка. Функцию log10 вы найдете в модуле math.

import math

def sum(a, b):
    return round(a + b, 2)
def sub(a, b):     
    return round(a - b, 2)
def mult(a, b):
    return round(a * b, 2)
def div (a, b):    
    return round(a / b, 2)
def floor_div(a, b):
    return a // b
def modulo(a, b):
    return round(a % b, 2)
def pow(a, b):
    return a ** b
def log_10(a):
    return round(math.log10(a), 2)


def less(a,b):
    return a < b
def less_equal(a, b):
    return a <= b
def greater(a, b):
    return a > b
def greater_equal(a, b):
    return a >= b
def not_equal(a, b):
    return a != b
def equal(a, b):
    return a == b

result_text = """
Арифмитические операторы:

Сумма: {sum}
Вычетание: {sub}
Умножение: {mult}
Деление: {div}
Деление с округлением: {floor_div}
Деление с остатком: {modulo}
Возведение в квадрат: {pow}
Десятичный логарифм первого числа: {log_10_a}
Десятичный логарифм второго числа: {log_10_b}

Операторы сравнения:
Первое число меньше второго: {less}
Первое число меньше или равно второго: {less_equal}
Первое число больше или равно второго: {greater_equal}
Числа не равны: {not_equal}
Числа равны: {equal}
"""

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


print(
    result_text.format( 
        sum = sum(a,b), 
        sub = sub(a,b), 
        mult = mult(a,b), 
        div = div(a,b), 
        floor_div = floor_div(a, b), 
        modulo = modulo(a,b), 
        pow = pow(a,b), 
        log_10_a = log_10(a), 
        log_10_b = log_10(b),
        less = less(a,b),
        less_equal= less_equal(a,b),
        greater = greater(a,b),
        greater_equal = greater_equal(a,b),
        not_equal = not_equal(a,b),
        equal = equal(a, b),
        )
    )