# functions/methods

# print(add(100, 200))
# print(add(300, 20))


# 1. static function
def greeting():
    return "Good Morning!"

# 2. dynamic function
def add(x, y):
    return x + y

# print(greeting())

a = 200
b = 400
# print(add(a, b))


def multiple(a, b):
    return a * b

# print(multiple(10, 50))

def table(m):
    for i in range(1, 11):
        print(f"{m} * {i} = {m*i}")
        
# table(5)

def is_even(num):
    return num % 2 == 0


# print(is_even(10))
# print(is_even(11))

# anonymous functions
is_even = lambda num: num % 2 == 0
# print(is_even(100))
# print(is_even(3))

# 1. filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# p -> filter even numbers from the above list using lambda function

# def filter_even(nums):
#     even = []
#     for i in nums:
#         if i % 2 == 0:
#             even.append(i)
#     return even 

# print(filter_even(nums))

even_nums_filter = list(filter(lambda num: num % 2 == 0, nums)) 
# print(even_nums_filter)

# 2. map

even_nums_map = list(map(lambda num: num % 2 == 0, nums))
# print(even_nums_map)


# p2 -> square each number in a list
nums = [2, 4, 5, 7]  # -> output [4, 16, 25, 49]

squares = list(map(lambda square: square**2, nums))
print(squares)

# p3 -> convert the strings in a list to int

ls = ["1", "2", "3"]  # -> output [1, 2, 3]

num_ls = list(map(int, ls))
print(num_ls)

# p4 -> remove empty strings
input = ["hi", "", "", "hello", "", "morning", "", ""]
input_ls = list(filter(lambda x: len(x) > 0, input))
print(input_ls)
