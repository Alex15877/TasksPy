from collections import Counter

mas1 = [0, 3, 10, 25, -54, 0, 165, 98]
mas2 = [987, 560, 34, 65, 12345, 0, 876, 560]
mas = (input("1. mas1 = [0, 3, 10, 25, -54, 0, 165, 98] \n"
             "2. mas2 = [987, 560, 34, 65, 12345, 0, 876, 560] \n"
             "Выберите один из массивов: "))
if mas == "1":
    print("Вы выбрали массив №1")
    while 1:
        array = input("\nВыберите одну из следующих операций: \n"
                  "1) Сумма четных чисел массива, \n"
                  "2) Сумма наибольшего и наймешего элементов,\n"
                  "3) Проверка на возрастание\n"
                  "4) Проверка на убывание\n"
                  "5) Найти колдичестно различных элементов\n"
                  "6) Определить есть ли повторяющиеся элементы\n"
                  "7) Удалить элемент массива\n"
                  "8)  Переставить элементы массива в обратном порядке\n"
                      "Операция № ")
        if array == '1':
            s = sum(i for i in mas1 if i % 2 == 0)
            print("\nСумма четных чисел массива = " + str(s))
        elif array == "2":
            maximum = max(mas1)
            minimum = min(mas1)
            res = maximum + minimum
            print(str(res))
        elif array == "3":
            grow = sorted(mas1)
            print("\nМассив отортирован по возростанию\n", grow)
        elif array == "4":
            wane = sorted(mas1, reverse=True)
            print("\nМассив отортирован по возростанию\n", wane)
        elif array == "5":
            search = input("\nВведите элемент,который нужно найти: ")
            c = search in mas1
            print(c)
        elif array == "6":
            repeat = Counter(mas1)
            repeat.most_common()
            print(repeat)
        elif array == "7":
            delete = int(input("\nВведите порядковый номер числа для удаления: "))
            l = (i for i in mas1 if i == delete)
            n = mas1.pop(delete - 1)
            print(mas1, "\n Вы удалили число " + str(n))
        elif array == "8":
            rev = mas1.reverse()
            print(mas1)
        else:
            print("\nНеверно введено число")
            break

elif mas == "2":
    while 2:
        print("Вы выбрали массив №1")
        array = input("\nВыберите одну из следующих операций: \n"
                      "1) Сумма четных чисел массива, \n"
                      "2) Сумма наибольшего и наймешего элементов,\n"
                      "3) Проверка на возрастание\n"
                      "4) Проверка на убывание\n"
                      "5) Найти колдичестно различных элементов\n"
                      "6) Определить есть ли повторяющиеся элементы\n"
                      "7) Удалить элемент массива\n"
                      "8)  Переставить элементы массива в обратном порядке\n"
                      "Операция № ")
        if array == '1':
            s = sum(i for i in mas2 if i % 2 == 0)
            print("\nСумма четных чисел массива = " + str(s))
        elif array == "2":
            maximum = max(mas2)
            minimum = min(mas2)
            res = maximum + minimum
            print(str(res))
        elif array == "3":
            grow = sorted(mas2)
            print("\nМассив отортирован по возростанию\n", grow)
        elif array == "4":
            wane = sorted(mas2, reverse=True)
            print("\nМассив отортирован по возростанию\n", wane)
        elif array == "5":
            search = input("\nВведите элемент,который нужно найти: ")
            c = search in mas1
            print(c)
        elif array == "6":
            repeat = Counter(mas1)
            repeat.most_common()
            print(repeat)
        elif array == "7":
            delete = int(input("\nВведите порядковый номер числа для удаления: "))
            l = (i for i in mas1 if i == delete)
            n = mas1.pop(delete - 1)
            print(mas2, "\n Вы удалили число " + str(n))
        elif array == "8":
            rev = mas2.reverse()
            print(mas2)
        else:
            print("\nНеверно введено число")
            break
else:
    print("Команда введина не правильно")