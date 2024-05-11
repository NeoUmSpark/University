n = input("Введите число о 3 до 20: ")
n = int(n)


result = ""
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if n % (i + j) == 0:
            result += str(i) + str(j)


print("Для числа", n, "пароль", result)
