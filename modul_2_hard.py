def find_password(n):
    if n < 3 or n > 20:
        return "Число n должно быть в диапазоне от 3 до 20."

    result = ""
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += f"{i}{j}"
    else:
        print("Ошибка: введите число от 3 до 20")

    return result

n = int(input("Dведите число от 3 до  20:"))


password = find_password(n)
print(f"Пароль для числа {n}: {password}")