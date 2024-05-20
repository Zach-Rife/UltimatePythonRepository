# ========== 4.4.1 ==========
# word = input("Please type in a string")
# for letter in word:
#     print(letter)

# ========== 4.4.2 ==========
# number = int(input("Please type in a positive intiger: "))
# num = number * -1
# for intiger in range(num, number + 1):
#     if intiger != 0:
#         print(intiger)

# ========== 4.4.3 ==========
# def list_of_stars(numbers):
#     numbers = []
#     for stars in numbers:
#         print("*" * stars)
# numbers = [3, 7, 1, 1, 2]
# list_of_stars(numbers)


# ========== 4.4.4 ==========

# word = "racecar"
# def palindromes(word):
#     half = len(word) // 2
#     backhalf = len(word)
#     for number in range(0, half + 1):
#         backhalf -= 1
#         if word[number] != word[backhalf]:
#             return False
#     return True

# print(palindromes("python"))
# print(palindromes("java"))
# print(palindromes("racecar"))
# print(palindromes("sailboats"))


    

# ========== 4.4.5 ==========
# def sum_of_positives(numbers):
#     total = 0
#     for intiger in numbers:
#         if intiger > 0:
#             total += intiger
#             print(total)
# numbers = [1, -2, 3, -4, 5]
# sum_of_positives(numbers)

# ========== 4.4.6 ==========
# def even_numbers(numbers):
#     even = []
#     for number in numbers:
#         if number % 2 == 0:
#             even.append(number)
#     print(even)
#     numbers = [1, 2, 3, 4, 5]
#     even_numbers(numbers)

# ========== 4.4.7 ==========
# def list_sum(a, b):
#     sum_list = []
#     index = 0
#     for number in a
#         sum = a[index] + b[index] 
#         index += 1
#         sum_list.append(sum)
#     print(sum_list)
# a = [1, 2, 3]
# b = [7, 8, 9]
# list_sum(a,b)
    

# ========== 4.4.8 ==========
# def length_of_longest(my_list):
#     total = 0 
#     longest = 0
#     for word in my_list:
#         total = 0
#         for letter in word:
#             total += 1
#             if total > longest:
#                 longest = total
#     return(longest)
# my_list = ["First", "Second", "fourth", "eleventh"]
# result = length_of_longest(my_list)
# print(result)
# ========== 4.4.9 ==========
def length_of_shortest(my_list): 
    shortest = "L" * 100000
    for word in my_list:
        total = len(word)
        if total < len(shortest):
            shortest = word
    return(shortest)
my_list = ["First", "Second", "fourth", "eleventh"]
result = length_of_shortest(my_list)
print(result)
