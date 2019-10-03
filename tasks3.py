from collections import Counter


mas1 = [0, 3, 10, 25, -54, 0, 165, 98]
mas2 = [987, 560, 34, 65, 12345, 0, 876, 560]
mas3 = [1, 2, 3, 4, 5, 45, 76]
mas4 = [54, 45, 22, 3, 1, 0, -10, -23]
mas = (input("1. mas1 = [0, 3, 10, 25, -54, 0, 165, 98] \n"
             "2. mas2 = [987, 560, 34, 65, 12345, 0, 876, 560] \n"
             "3. mas3 = [1, 2, 3, 4, 5, 45, 76]\n"
             "4. mas4 = [54, 45, 22, 3, 1, 0, -10, -23]\n"
             "Выберите один из массивов: "))
if mas == "1":
    print("Вы выбрали массив №1")
    sel_mas = mas1
elif mas == "2":
    print("Вы выбрали массив №2")
    sel_mas = mas2
elif mas == "3":
    print("Вы выбрали массив №3")
    sel_mas = mas3
elif mas == "4":
    print("Вы выбрали массив №4  ")
    sel_mas = mas4
else:
    print("Команда введина не правильно")
while True:
    array = input("\nВыберите одну из следующих операций: \n"
                  "1) Сумма четных чисел массива, \n"
                  "2) Сумма наибольшего и наймешего элементов,\n"
                  "3) Сортировка по возрастанию и убыванию\n"
                  "4) Проверка на возростание\n"
                  "5) Найти колдичестно различных элементов\n"
                  "6) Определить есть ли повторяющиеся элементы\n"
                  "7) Удалить элемент массива\n"
                  "8)  Переставить элементы массива в обратном порядке\n"
                      "Операция № ")
    if array == '1':
        s = sum(i for i in sel_mas if i % 2 == 0)
        print("\nСумма четных чисел массива = " + str(s))
    elif array == "2":
        maximum = max(sel_mas)
        minimum = min(sel_mas)
        res = maximum + minimum
        print(str(res))
    elif array == "3":
        deb = input("Сортировать по возростанию(+)\n"
                    "Сортировать по убыванию(-)\n"
                    "Сортировка : ")
        if deb == "+":
            grow = sorted(sel_mas)
            print("\nМассив отортирован по возростанию\n", grow)
        elif deb == "-":
            wane = sorted(sel_mas, reverse=True)
            print("\nМассив отортирован по возростанию\n", wane)
        else:
            print("Нужно ввести знак '+' или '-'")
    elif array == "4":
        zip(sel_mas, sel_mas[1:])
        all(x <= y for x, y in zip(sel_mas, sel_mas[1:]))
        print(all(sel_mas))
    elif array == "44":
        # это должно было быть на убывание
        zip((sel_mas, sel_mas[:-1]))
        all(x >= y for x, y in zip(sel_mas, sel_mas[:-1]))
        print(all(sel_mas))
    elif array == "5":
        c = Counter(sel_mas)
        fer = list(c)
        print(fer)
    elif array == "6":
        repeat = Counter(sel_mas)
        repeat.most_common()
        print(repeat)
    elif array == "7":
        delete = int(input("\nВведите порядковый номер числа для удаления: "))
        l = (i for i in sel_mas if i == delete)
        n = sel_mas.pop(delete - 1)
        print(sel_mas, "\n Вы удалили число " + str(n))
    elif array == "8":
        sel_mas.reverse()
        print(sel_mas)
    else:
        print("\nНеверно введено число")
        break