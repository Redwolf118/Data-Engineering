# 4. Работа с массивами
# Создайте JSON-файл, содержащий список словарей с информацией о книгах (название, автор, год издания). 
# Добавьте функцию для поиска книг по автору.

import json
def load_books(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)

def find_books_by_author(books, author):
    result = []
    for book in books:
        if "Автор" not in book:
            continue
        if author.lower() in book["Автор"].lower():
            result.append(book)

    return result


if __name__ == "__main__":
    filename = "data.json"
    books = load_books(filename)
    
    author = input("Введите имя автора для поиска: ")
    found_books = find_books_by_author(books, author)


    json_write = "found_books.json"

    with open(json_write, 'w') as file:
        json.dump(found_books, file, ensure_ascii=False, indent=4)

    print(f"Книги автора {author} сохранены в файле {json_write}")
