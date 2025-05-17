try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
    print(f"Результат деления: {result}")
except ValueError:
    print("Ошибка: Введите числа, а не текст!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")
finally:
    print("Программа завершена. Спасибо за использование!")
