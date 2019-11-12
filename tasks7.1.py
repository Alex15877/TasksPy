# Добавить одно свойство и один метод, позволяющий его менять.
# Создать третий объект и изменить все его свойства.

class Second:
    color = 'red'
    form = 'circle'
    size = 'small'
    def changecolor(self, newcolor):
        self.color = newcolor
    def changeform(self, newform):
        self.form = newform
    def changesize(self, newsize):
        self.size = newsize

obj1 = Second()
obj2 = Second()
obj3 = Second()

print(obj1.color, obj1.form, obj1.size)
print(obj2.color, obj2.form, obj2.size)
print(obj3.color, obj3.form, obj3.size)

obj1.changecolor('green')
obj2.changecolor('blue')
obj2.changeform('oval')
obj2.changesize('normal')
obj3.changecolor('black')
obj3.changeform('cube')
obj3.changesize('big')

print(obj1.color, obj1.form, obj1.size)
print(obj2.color, obj2.form, obj2.size)
print(obj3.color, obj3.form, obj3.size)
