class Animal:
    a = 1

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def make_sound(self):
        print(f'Sound Animal {self.name}')


class Cat(Animal):
    def make_sound(self):
        print(f'Sound Cat {self.name}')


class Dog(Animal):
    def make_sound(self):
        print(f'Sound Dog {self.name}')

    def __str__(self):
        return f'Dog({self.name})'

a1 = Cat('Vasya', 3, 50)
a2 = Dog('Petya', 14, 10)
a3 = Dog('Petya2', 14, 10)

print(a1)
print(a2)
print(a3)
