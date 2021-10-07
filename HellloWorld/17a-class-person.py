class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'Hi , I am  {self.name}')


person = Person('John')
person.talk()

person = Person('Bob')
person.talk()