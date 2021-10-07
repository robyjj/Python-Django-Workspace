class Animal:
    def walk(self):
        print('Walk')

class Dog(Animal):
    def bark(self):
        print('Bow')

class Cat(Animal):
    def meow(self):
        print('Meow')
    def walk(self):
        print('Cat walk')


cat = Cat()
cat.walk() #Cat walk
cat.meow() #Meow






