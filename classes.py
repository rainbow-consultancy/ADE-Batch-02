# class

# class House:
#     pass

class House:
    def get_name(self):
        return "Brundhawan House"

# cls_obj = House()
# print(cls_obj.get_name())
company = "Rainbow"  # global variable

class Student:
    def __init__(self, name, age):
        self.name = name # public variable
        self.age = age
        # print("InIt method is called")

    def get_student_name(self):
        return f"Student name is - {self.name}"

    def get_student_age(self):
        return f"Student age is - {self.age}"
    
    def get_global_var(self):
        return f"Global Var - {company}"

manoj_obj = Student("Manoj", 20)
# gagan_obj = Student("Gagan", 21)

# print(manoj_obj.get_student_name())
# print(gagan_obj.get_student_name())

print(manoj_obj.get_global_var())


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private variable
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount Deposited - {amount}")
    
    def __fetch_details(self):
        return f"Acc holder name is {self.name}"
    
    def show_balance(self):
        print(f"Balance is: {self.__balance}")
        print(self.__fetch_details())
        

acc1 = BankAccount("Sathvika", 5000)
# print(acc1.__balance)
acc1.deposit(3000)
acc1.show_balance()
# acc1.__fetch_details()

# acc2 = BankAccount("Teja", 10000)
# print(acc2.balance)
# acc2.deposit(4000)
# acc2.show_balance()



# Variables

# 1. global variable --> this variables can be access anywhere
# 2. public variable --> this variables can be accessed with in class or a method/function
# 3. private variable --> this variable can be used only inside the class
