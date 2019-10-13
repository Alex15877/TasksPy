print("Заполните базу следующим образом(Покупатель, название товара, количество товара)\n")


def func(x):
    buy = {}
    for i, j in x:
        prod, count = i, int(j)  # присвоени значений(товар, количество)
        if prod in buy:
            buy[prod] += count
        else:
            buy[prod] = count
    return buy


base = {}
while True:
    try:
        man, prod, count = input().split()  # вводим покупателей, товары и их количество
        if man in base:
            base[man].append((prod, count))
        else:
            base[man] = [(prod, count)]
    except:
        break

for i in sorted(base):
    print(i + ':')  # выводим покупателя
    for x, i in sorted(func(base[i]).items()):
        print(x, i)