# ========== 4.3.1 ==========
# number_list = [1, 2, 3, 4, 5]
# while True:
#     index = int(input("Index"))
#     if index == -1:
#         break
#     else:
#         number = int(input("number"))
#         number_list.pop(index)
#         number_list.insert(index, number)
#         print(number_list)
# ========== 4.3.2 ==========
list = []
item = int(input("How many items "))
total = 0
while True:
    i1 = int(input("item")) 
    list.append(i1)
    total += 1
    if total == item:
        break
print(list)
# ========== 4.3.3 ==========
# list3 = []
# total = 1
# while True:
#     edit = print("a(d)d, (r)emove or e(x)it")
#     if edit == "d":
#         list3.append(total)
#         total += 1
#     elif edit == "r":
#         list3.remove(len(list3)-1)
#         total -= 1
#     else:
#         break
# print("Bye")

# ========== 4.3.4 ==========
# number = []
# total = -1
# while True:
#     word = input("Please type in a word")
#     total += 1
#     if word in number:
#         break
#     number.append(word)
# print("You typed in", total, "differint words")
    