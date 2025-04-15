class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

# Creating object
my_car = Car("Toyota", "Corolla")
my_car.drive()


class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

d = Dog()
d.speak()  # Output: Dog barks.

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())  # Output: 1000


class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def animal_sound(animal):
    animal.sound()

animal_sound(Cat())
animal_sound(Dog())

