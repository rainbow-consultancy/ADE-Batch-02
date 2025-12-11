# Polymorphism --> same name but it changes/behaves differently

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

class Animal:
    def sound(self):
        print("Animal Sound")

cat_obj = Cat()
# cat_obj.sound()

dog_obj = Dog()
# dog_obj.sound()

ani_obj = Animal()
# ani_obj.sound()

# method overloading
#  ---- In python method overloading does not exists

def add(a, b, c=0):
    print(a+b+c)


# add(10, 30, 60)
# add(10, 30)

# method overriding

class Vehicle:
    def start(self):
        return "Vehicle Starting"
    
    def stop(self):
        return "Stopped"

class Car(Vehicle):
    def start(self):
        return "Car Engine Starting"

v = Vehicle()
c = Car()

# print(v.start())
# print(v.stop())
# print(c.start())
# print(c.stop())
    

# abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class UPI(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI"

p = UPI()
print(p.pay(500))
