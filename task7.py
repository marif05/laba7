text = input("Введите строку: ")

# Очистка текста от пробелов
text = text.lower().replace(" ", "")

# Подсчет гласных и согласных
vowels = 0
consonants = 0
for char in text:
    if char in "аеёиоуыэюя":
        vowels += 1
    elif char in "бвгджзклмнпрстфхцчшщъыьэю":
        consonants += 1
        
print(f"В строке '{text}':")
print(f"- Гласных: {vowels}")
print(f"- Согласных: {consonants}")
