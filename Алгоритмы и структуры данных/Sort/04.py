# Сортировка по частоте встречаемости
# Задача: отсортировать список слов по частоте их встречаемости в тексте.
# Пример: ["apple", "banana", "apple", "cherry", "banana"] → ["apple", "banana", "cherry"]

def sort_by_count(words):
    count = dict()
    unique_words = list()
    
    # Считаем частоту и сохраняем порядок появления
    for word in words:
        if word not in count:
            count[word] = 1
            unique_words.append(word)  # добавляем уникальное слово один раз
        else:
            count[word] += 1
    
    # Сортировка вставками
    n = len(unique_words)
    for i in range(1, n):
        key = unique_words[i]
        j = i - 1
        while j >= 0 and count[unique_words[j]] < count[key]: 
            unique_words[j + 1] = unique_words[j]
            j -= 1
        unique_words[j + 1] = key
    
    return unique_words

words = ["apple", "banana", "apple", "cherry", "banana"]
res = sort_by_count(words)
print(res) 