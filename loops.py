# loops 

# 1. for loop
# 2. while loop

# 1. for loop
# syntax
# for i in range(start=0:stop:step=1)

# for i in range(0, 10, 2):
#     print("SSS")

# for i in range(10):
#     print("SSS")


# while loop
# x = 'abc'
# c = 1

# while c <= 5:
#     print(x)
#     c = c + 1



# for i in range(1, 101):
#     if i == 10:
#         break
#     else:
#         print(i)

# for i in range(1, 21):
#     if i == 10:
#         continue
#     else:
#         print(i)

# start = 1

# while start < 10:
#     print(start)
#     # start = start + 1
#     start += 1


# print 2 table
# 2 * 1 = 2
# 2 * 2 = 4
# .
# .
# 2 * 10 = 20        

# 4 * 1 = 4
# 4 * 2 = 8
# print(2)

# 2 * 1 = 2


# for i in range(1, 11):
#     print("2 *", i, "=", 2*i)
    
    
# for j in range(1, 11):
#     print("4 *", j, "=", 4*j)
    

# print(f"2 * {i} = {2 * i}")

# string formatters
# for j in range(1, 11):
#     print("4 * {0} = {1}".format(j, 4*j))
    
# for j in range(1, 11):
#     print(f"4 * {j} = {4*j}")

# 2 to 5 tables


# for i in range(2, 6):
#     print(f"{i} - Table")
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#     print("---------------------------------")


# for i in range(2, 11, 2):
#     for j in range(1, 6):
#         print("{0} * {1} = {2}".format(i, j, i*j))
#     print("---------------------")
    

# for i in range(2, 11):
#     if i%2 == 0:
#         for j in range(1, 6):
#             print("{0} * {1} = {2}".format(i, j, i*j))
#         print("---------------------")


name = input("Enter a name: ")

vowels = ['a', 'e', 'i', 'o', 'u']

cnt = 0
for i in name.lower():
    if i in vowels:
        cnt+=1
        
print(cnt)






