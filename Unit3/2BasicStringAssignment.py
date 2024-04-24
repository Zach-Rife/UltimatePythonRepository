# ========== 3.2.1 ==========
# string = input("Please type in a string")
# amount = int(input("Please type in a amount"))
# print(string * amount)

# # ========== 3.2.2 ==========
# word1 = input("Please type in string 1; ")
# word2 = input("Please type in string 2; ")
# if len(word1) > len(word2):
#     print(word1, "Is longer")
# elif len(word2) > len(word1):
#     print(word2, "Is longer")
# else:
#     print("They are both equally long")

# # ========== 3.2.3 ==========
# word = input("Please type in a string")
# num1 = len(word)
# num = len(word)
# total = 0
# while total < num:
#     num = num - 1
#     print(word[num])
#     total = total + 1
#     if total == num1:
#         break
    
    

# # ========== 3.2.4 ==========
# word = input("Please type in a string")
# if word[1] == word[-2]:
#     print("The second and the second to last characters are", word[1])
# else:
#     print("The second and the second to last characters are differint")

# ========== 3.2.5 ==========
# num = int(input("Width"))
# print("#" * num)

# # ========== 3.2.6 ==========
# width = int(input("Width"))
# height = int(input("height"))
# num = height
# while True:
#     print("#" * width)
#     num = num - 1
#     if num == 0:
#         break
# # ========== 3.2.7 ==========
# while True:
#     word = input("Please type in a string")
#     print(word)
#     print("-" * len(word))
#     if word == "":
#         break

# # ========== 3.2.8 ==========
# word = input("Please type in a string")
# length = len(word)
# print("*" * (20 - length) + word)

# ========== 3.2.9 ==========
word = input("Please type in a string")
length = len(word)
print("*" * 30)
print("*" + " " * (15 - length//2) + word + " " * (15 - length//2) + "*")
print("*" * 30)
