number = int(input("Введите целое число больше 1: "))

# Проверка на простоту
is_prime = True
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"Число {number} является простым.")
else:
    print(f"Число {number} не является простым.")
