# OOPS - Object Oriented Programming
class Student:
    pass


# OOPS - Encapsulation, Inheritence, Polymorphism, Abstraction

# 1. Encapsulation  -> Protecting Importent Information

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private variable
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount Deposited - {amount}")

obj = BankAccount("Sandeep", 2000)
# print(obj.name)

# 2. Inheritence (single, multiple, multilevel and hybrid)

class Father:  # base class / parent class
    def get_fathers_properties(self):
        print("Owns Complex in HSR Layout")
        
class Child(Father):  # -- inherited from father's class' child class/derived class
    def get_child_properties(self):
        print("Owns a Car")

# obj_child = Child()
# obj_child.get_child_properties()
# obj_child.get_fathers_properties()

# multiple
class Father:  # base class / parent class
    def get_fathers_properties(self):
        print("Owns Complex in HSR Layout")
    
class Mother:
    def get_mothers_properties(self):
        print("Owns Villa in HSR Layout")
        
class Child(Father, Mother):  # -- inherited from father's class' child class/derived class
    def get_child_properties(self):
        print("Owns a Car")

# obj_child = Child()
# obj_child.get_child_properties()
# obj_child.get_fathers_properties()
# obj_child.get_mothers_properties()

# multi-level
class Father:  # base class / parent class
    def get_fathers_properties(self):
        print("Owns Complex in HSR Layout")
    
class Mother(Father):
    def get_mothers_properties(self):
        print("Owns Villa in HSR Layout")
        
class Child(Mother):  # -- inherited from father's class' child class/derived class
    def get_child_properties(self):
        print("Owns a Car")

# obj_child = Child()
# obj_child.get_child_properties()
# obj_child.get_fathers_properties()
# obj_child.get_mothers_properties()


# Polymorphisam  - same action different meaning

# live 

class Teacher:
    def work(self):
        print("Teaching Students")

class Developer:
    def work(self):
        print("Writing code")
        
# obj1 = Teacher()
# obj1.work()

# obj2 = Developer()
# obj2.work()


class Cal():
    
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

obj = Cal()
# print(obj.add(10, 20))
print(obj.add(10, 20, 30))