from collections import Counter

mas1 = [0, 3, 10, 25, -54, 0, 165, 98]
mas2 = [987, 560, 34, 65, 12345, 0, 876, 560]
mas = (input("1. mas1 = [3, 10, 25, -54, 0, 165, 98] \n"
             "2. mas2 = [ 987, 34, 65, 12345, 0, 876, 560] \n"
             "Выберите один из массивов: "))
if mas == "1":
    print("Вы выбрали массив №1")
    array = input("\nВыберите одну из следующих операций: \n"
                  "1) Сумма четных чисел массива, \n"
                  "2) Сумма наибольшего и наймешего элементов,\n"
                  "3) Проверка на возрастание\n"
                  "4) Проверка на убывание\n"
                  "5) Найти колдичестно различных элементов\n"
                  "6) Определить есть ли повторяющиеся элементы\n"
                  "7) Удалить элемент массива\n"
                  "8)  Переставить элементы массива в обратном порядке")
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
        print("\nМассив отортирован по возростанию\n",grow)
    elif array == "4":
        wane = sorted(mas1, reverse = True)
        print("\nМассив отортирован по возростанию\n",wane)
    elif array == "5":
        u = input("\nВведите элемент,который нужно найти: ")
        c = u in mas1
        print(c)
    elif array == "6":
        got = Counter(mas1)
        got.most_common()
        print(got)

    elif array == "7":
        d = int(input("\nВведите порядковый номер числа для удаления: "))
        l = (i for i in mas1 if i == d)
        n = mas1.pop(d-1)
        print(mas1, n)
    elif array == "8":
        r = mas1.reverse()
        print(mas1)
    else:
        print("\nНеверно введено число")


  # b = (i for i in mas1 if [i] <= [i+1])
          #  print(mas1, b)

  #  elif array == "6":
   #     [j for j in mas1 if mas1[j] > 1]


           #for m in mas1:
             #   if m % 2 == 0:
              #      print(format(m))
                #    if m != 0:
                 #       print("1")

                    #continue
                #elif min(mas1):
                #    print(min(mas1))
                 #   break

#elif mas == "2":
 #  print("Вы выбрали массив №2")
  #  for mm in mas2:
   #     if len(str(mm)) != input("С каким количеством символов вы хотите вывести слова(Укажите число)"):
    #        print(type(mm))
     #   else:
      #      print("чччч")
    #else:
     #   print("Не правильно введена команда")

