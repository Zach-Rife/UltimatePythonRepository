# ========== 3.3.1 ==========
# word = input("Please type in a string")
# number = 0
# number2 = 0
# while True:
#     print(word[number:number2])
#     number2 = number2 + 1
#     if number2 == len(word) + 1:
#         break


# ========== 3.3.2 ==========
# word = input("Please type in a string")
# number = len(word)
# while True:
#     print(word[number])
#     number = number - 1
#     if number < 0
#         break

# ========== 3.3.3 ==========
# word = input("Please type in a string")
# if  "a" in word:
#     print("a found")
# else:
#     print("a not found")
# if  "e" in word:
#     print("e found")
# else:
#     print("e not found")
# if  "o" in word:
#     print("o found")
# else:
#     print("o not found")



# ========== 3.3.4 ==========
# word = input("Please type in a string")
# char = input("Please type in a character")
# char1 = word.find(char)
# if char1 + 3 > len(word):
#     print(" ")
# else:
#     print(word[char1:char1+3])

# ========== 3.3.5 ==========
# word = input("Please type in a word")
# char = input("Please type in a character")
# while True:
#     char1 = word.find(char)
#     if char1 == -1:
#         break
#     elif len(word) < 3:
#         break
#     else:
#         print(word[char1:char1+3])
#         word = word[char1+1:]

    

# ========== 3.3.6 ==========
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
pos = string.find(substring)
pos1 = pos
if pos >= 0:
    string = string[pos+1:]
    pos = string.find(substring)
    pos1 = pos1 + pos
    if pos >= 0:
        print("The second occurrence of the substring is at index", pos1 + 1)
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")

