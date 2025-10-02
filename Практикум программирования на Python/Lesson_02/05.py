# Задача 5.
# Мы пишем приложение для удобного прослушивания музыки. 
# У Вани есть список из девяти песен группы Depeche Mode. 
# Каждая песня состоит из названия и продолжительности с точностью до долей минут:
# violator_songs = [
#     ['World in My Eyes', 4,86],
#     ['Sweetest Perfection', 4,43],
#     ['Personal Jesus', 4,56],
#     ['Halo', 4,9],
#     ['Waiting for the Night', 6,07],
#     ['Enjoy the Silence', 4,20],
#     ['Policy of Truth', 4,76],
#     ['Blue Dress', 4,29],
#     ['Clean', 5,83]
# ]

# Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками. 
# И при этом ему важно, сколько времени в сумме эти N песен будут звучать.
# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен, 
# а на экран выводит общее время их звучания.


# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean

# Общее время звучания песен: 14,93 минуты


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_songs = int(input("Сколько песен выбрать? "))
total_time = 0.0
for i in range(1, num_songs + 1):
    song_name = input(f"Название {i}-й песни: ")
    for song in violator_songs:
        if song[0].lower() == song_name.lower():
            total_time += song[1]
            break

print(f"\nОбщее время звучания песен: {round(total_time, 2)} минуты")