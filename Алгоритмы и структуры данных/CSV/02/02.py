# 2. Запись в CSV
# Создать программу, которая записывает список словарей с информацией о книгах в CSV файл.

# books = [
#     {'title': 'Война и мир', 'author': 'Толстой', 'year': 1869},
#     {'title': '1984', 'author': 'Оруэлл', 'year': 1949}
# ]

import csv

books = [
    {'title': 'Война и мир', 'author': 'Толстой', 'year': 1869},
    {'title': '1984', 'author': 'Оруэлл', 'year': 1949}
]

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
    writer.writeheader()
    writer.writerows(books)


