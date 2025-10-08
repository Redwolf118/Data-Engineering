# Упражнение 7. 
# Строка называется палиндромом, если она пишется одинаково в обоих направлениях. 
# Например, палиндромами в английском языке являются слова «anna», «civic», «level», «hannah». 
# Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую, является ли она палиндромом.

def is_palindrome(s):
    s = s.lower()
    length = len(s)
    
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Это палиндром")
else:
    print("Это не палиндром")
