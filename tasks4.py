while True:
    try:
        oper = input("Выберите опреацию (+, -, *, /): ")
    except ValueError:
        print("Выберите операцию из указаных выше.")
        continue
    firstdigit = float(input("Введите первое число:"))
    seconddigit = float(input("Введите второе число:"))
    if oper == "+":
        result = firstdigit + seconddigit
        print("Результат: " + str(result))
    elif oper == "-":
        result = firstdigit - seconddigit
        print("Результат: " + str(result))
    elif oper == "*":
        result = firstdigit * seconddigit
        print("Результат: " + str(result))
    elif oper == "/":
        result = firstdigit / seconddigit
        print("Результат: " + str(result))
    else:
        print("Выбрана неверная операция!\n"
              "Не целые числа вводятся через точку(.)")
    break
