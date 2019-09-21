name = str(input("Введите свое имя:"))
print("Привет " + name)

while True:
    try:
        age = int(input("Введите свой год рождения: "))
    except ValueError:
        print("Вы ввели некоректные данные")
        continue
    else:
        break

if len(str(age)) != 4:
    print("Вы ввели не 4 цыфры")
elif age <= 1920:
    print("Вы ввели не верный год.")
elif age > 2019:
    print("Этот год еще не настал")
else:
        print('Круто!')

year = 2019 - int(age)
print("Вам уже :" + str(year))
if year < 18:
    print("Вы еще несовершеннолетний. Вам отказано в посещении клуба.")
elif year > 100:
    print("Кажется, Вас обыскались на кладбище")
else:
    print("Вы совершеннолетний, можете войти в клуб.")

