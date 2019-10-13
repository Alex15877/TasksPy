while True:
    try:
        op = int(input("Выберите опреацию: 1) +, 2) -, 3) *, 4) /): "))
    except ValueError:
        print("Выберите операцию из указаных выше.")
        continue
    d = [(1, chr(43)), (2, chr(45)), (3, chr(42)), (4, chr(47))]
    firstdigit = float(input("Введите первое число:"))
    seconddigit = float(input("Введите второе число:"))
    g = op in d
    res = firstdigit + g + seconddigit
    print(res)
    break
