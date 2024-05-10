# ========== 4.1.1 ==========
def line(times, text):
    if text == "":
        print("*" * times)
    else:
        print(text[0] * times)
# times = int(input("number"))
# text = input("Text")
# line(times, text)

# ========== 4.1.2 ==========
# def box_of_hashes(height):
#     count = 0
#     while True:
#         line(10, "#")
#         count += 1
#         if count >= height:
#             break
# box_of_hashes(5)

# # ========== 4.1.3 ==========
# def square_of_hashes(height):
#     count = 0
#     while True:
#         line(times, "#")
#         count += 1
#         if count >= height:
#             break
# square_of_hashes(5)

# # ========== 4.1.4 ==========
# def square(times, text):
#     count = 0
#     while True:
#         line(times, text)
#         count += 1
#         if count >= times:
#             break
# square(5, "*")

# ========== 4.1.5 ==========
# def triangle(times):
#     count = 0
#     num = 1
#     while True:
#         line(num, "#")
#         count += 1
#         num += 1
#         if count >= times:
#             break
# triangle(6)

# ========== 4.1.6 ==========
# def shape(num1, let1, num2, let2):
#     count = 1
#     while count < num1 + 1:
#         line(count, let1)
#         count += 1
#     count = 0
#     while count < num2:
#         line(num1, let2)
#         count+=1
# shape(5, "x", 3, "*")

# ========== 4.1.7 ==========
def spruce(width):
    count = 0
    num = 1
    space = width
    while count < width:
        print(" " * (space-1), "*" * num)
        num += 2
        count += 1
        space += 1
        print()


        
        
  
        
spruce(3)