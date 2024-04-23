text = input("Введите строку: ")

# Очистка текста от пробелов, знаков препинания и регистра
text = text.lower().replace(" ", "").replace(",", "").replace(".", "")

# Проверка на палиндром
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"Строка '{text}' является палиндромом.")
else:
    print(f"Строка '{text}' не является палиндромом.")
