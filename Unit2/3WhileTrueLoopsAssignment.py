# ========== 2.3.1 ==========
# input()
# while True:
#     word = input("Shall we continue?")
#     if word == "no":
#       print("Okay then") 
#       break
#     else:
#         print("Hi")



# ========== 2.3.2 ==========
# from math import sqrt
# while True:
#     num = int(input("Please type in a number "))
#     if num < 0:
#         print("Invalid number")
#     elif num == 0:
#         print("Exiting")
#         break
#     else:
#         print(sqrt(num))

# ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number == 0:
#     break

# print("Now!")

# ========== 2.3.4 ==========
# password = input("Password:")
# while True:
#     word = input("Repeat Password:")
#     if password == word:
#         print("User account created!")
#     else:
#         print("They do not match")

# ========== 2.3.5 ==========
# pin = int(4321)
# attempt = 0
# while True:
 
#     pinguess = int(input("Pin"))
#     attempt = attempt + 1
#     if pin == pinguess and attempt == 1:
#         print("Correct! It only took you a single attempt")
#     elif pin == pinguess:
#         print("Correct It took you ", attempt, "Attempts")



# ========== 2.3.6 ==========
# year = int(input("Year"))
# leap = year + 1
# while True:
#  if leap % 4 == 0:
#     print("The next leap year after",  year, "is", leap)
#     break
#  else:
#     leap = leap + 1
# ========== 2.3.7 ==========
# word = input("Please type in a word: ")
# sentence =  word + " "
# while True:
#     word = input("Please type in a word: ")
#     if word == "end":
#         print(sentence)
#         break
#     else:
#         sentence = sentence + word + " "
# ========== 2.3.8 ==========
# word = input("Please type in a word: ")
# sentence =  word + " "
# word2 = word
# while True:
#     word = input("Please type in a word: ")
#     if word == "end" or word == word2:
#         print(sentence)
#         break
#     else:
#         sentence = sentence + word + " "
#         word2 = word
# ========== 2.3.9 ==========
print("Please type in integer numbers. Type in 0 to finish.")
total = 0
sum = 0
mean = 0
pos = 0
neg = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    else:
        total = total + 1
        sum = number + sum
    if number < 0:
        neg = neg + 1
    if number > 0:
        pos = pos + 1
    print("Numbers typed in:", total)
    print("Sum of numbers:", sum)
    print("Mean of numbers:", sum/total)
    print("Positive numbers:", pos)
    print("Negative numbers:", neg)