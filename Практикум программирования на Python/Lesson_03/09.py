# Упражнение 9.
# Напишите программу, которая позволит пользователю преобразовывать числа из одной системы счисления в другую произвольным образом. 
# Ваша программа должна поддерживать все системы счисления в диапазоне от 2 до 16 как для входных, так и для выходных данных. 
# Если пользователь выберет систему с основанием, выходящим за границы допустимого, на экран должна быть выведена ошибка. 

# Разделите код программы на несколько функций, включая функцию, конвертирующую число из произвольной системы счисления в десятичную, 
# и обратную функцию, переводящую значение из десятичной системы в произвольную. 
# В основной программе необходимо запросить у пользователя исходную систему счисления, целевую систему, 
# а также число для преобразования.

def convert_to_decimal(num, base): 
    try: 
        return int(num, base) 
    except ValueError: 
        return None 
 
def convert_from_decimal(num, base): 
    digits = "0123456789ABCDEF" 
    if num == 0: 
        return "0" 
    result = "" 
    while num > 0: 
        result = digits[num % base] + result 
        num //= base
    return result 
 


# Функция для получения корректного основания системы счисления от пользователя
def get_base(prompt):
    while True:
        try:
            base = int(input(prompt))
            if 2 <= base <= 16:
                return base
            print("Ошибка: основание должно быть числом от 2 до 16.")
        except ValueError:
            print("Ошибка: введите целое число от 2 до 16.")

source_base = get_base("Введите основание исходной системы счисления (2–16): ")
target_base = get_base("Введите основание целевой системы счисления (2–16): ")

number = input("Введите число для преобразования: ").strip().upper()

decimal_number = convert_to_decimal(number, source_base)

if decimal_number is None:
    print(f"Ошибка: '{number}' не является допустимым числом для системы с основанием {source_base}.")
else:
    converted_number = convert_from_decimal(decimal_number, target_base)
    print(f"Число {number} в системе с основанием {source_base} равно {converted_number} в системе с основанием {target_base}.")
 
