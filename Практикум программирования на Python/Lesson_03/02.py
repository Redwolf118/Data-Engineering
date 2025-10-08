# Упражнение 2.
# Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру.

sentences = [
    "Первое предложение",
    "2 предложение",
    "1234556",
    "2 + 2 = 4",
    "Python3.10"
]

count = 0

for sentence in sentences:
    if any(ch.isdigit() for ch in sentence):
        count += 1

print("Количество предложений с цифрами:", count)