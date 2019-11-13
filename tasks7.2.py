# Написать программу в стиле ООП, которая удовлетворяет следующие условия:
# В программе должно быть 2 класса и 2 объекта, принадлежащих к разным классам
# Один объект с помощью метода своего класса должен изменять данные другого объекта.


class Teapot:
    water = 1000     # один литр
    water_temp = 40

    def put_the_teapot(self, water_temp):
        self.water_temp = water_temp

    def boils(self, water):
        self.water = water


class BoilsTeapot(Teapot):
    def put_the_teapot(self):
        self.water_temp += self.water_temp
        return self.water_temp + 20

    def boils(self):
        return self.water - 0.2


t = Teapot()
b = BoilsTeapot()
print('Было:')
print(t.water, 'мл воды')
print(t.water_temp, 'градусов (темпаратура воды)')
print("Стало:")
print(b.boils(), 'мл воды')
print(b.put_the_teapot(), 'градусов (темпаратура воды)')

