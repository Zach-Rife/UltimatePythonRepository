# ========== 3.1.1 ==========
# number = 0 
# while number < 30:
#     number = number + 2
#     print(number)
   


# ========== 3.1.2 ==========

# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number > 1:
#     number = number - 1
#     print(number)
# print("Go!")

# ========== 3.1.3 ==========
# number = int(input("Upper limit "))
# num = 0 
# while number > 0:
#     num = num + 1
#     if num < number:
#         print(num)

# ========== 3.1.4 ==========
# number = int(input("Upper limit "))
# num = 1
# while number > 0:
#     num = num * 2
#     if num < number:
#         print(num)

# ========== 3.1.5 ==========
# number = int(input("upper limit: "))
# base = int(input("base: "))
# num = 1
# print(num)
# while number > 0:
#     num = num * base 
#     if num <= number:
#         print(num)
# ========== 3.1.6 ==========
number = int(input("Limit: "))
num = 0
total = 0
while number > num:
    if number > num:
        total = total + 1
        num = num + total
    else:
        break
print(num)