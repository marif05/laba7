n = int(input("Введите целое неотрицательное число: "))

# Вычисление факториала
factorial = 1
if n == 0:
    factorial = 1
else:
    for i in range(1, n + 1):
        factorial *= i

print(f"Факториал числа {n} равен {factorial}")
