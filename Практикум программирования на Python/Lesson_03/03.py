# Упражнение 3.
# Дана строка s и символ k. Реализуйте функцию, рисующую рамку из символа k вокруг данной строки, например:

# **************
# *Текст в рамке*
# **************

def draw_frame(s, k):
    length = len(s) + 4  
    border = k * length  
    middle = f"{k} {s} {k}" 

    print(border, middle, border, sep="\n")

s = input("Введите строку: ")
k = input("Введите символ для рамки: ")
draw_frame(s, k)

    
