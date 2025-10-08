# Упражнение 5.
# Используя шифр Цезаря (достаточно только букв русского алфавита, знаки препинания не изменяются), 
# зашифруйте, а затем расшифруйте введенную строку.

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if 'а' <= char <= 'я':
            shifted = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            result += shifted
        elif 'А' <= char <= 'Я':
            shifted = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            result += shifted
        else:
            result += char
    return result

text = input("Введите текст для шифрования: ")
shift = int(input("Введите сдвиг (целое число): "))

encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Расшифрованный текст:", decrypted_text)
