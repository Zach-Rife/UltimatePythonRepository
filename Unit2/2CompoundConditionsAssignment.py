# # print("########## 2.2.1 ##########")
# age = int(input("What is your age?"))
# if age >= 5:
#     print("ok, youre", age, "years old")
# elif age < 5 and age > 0:
#     print("I suspect you can't write quite yet...")
# else:
#     print("Their must be a mistake")
# print("########## 2.2.2 ##########")
name = input("Please type in your name")
if name == "Huey" or name == "Dewey"  or name ==  "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")
# print("########## 2.2.3 ##########")
grade = float(input("Type in percent:"))
if grade > 100 or grade < 0:
    print("Impossiblr!")
if grade >= 90:
    print("Grade: A")
if grade >= 80:
    print("Grade: B")
if grade >= 70:
    print("Grade: C")
if grade >= 60:
    print("Grade: D")
if grade >= 0:
    print("Grade: F")

# print("########## 2.2.4 ##########")
number = int(input("number"))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print("  ")
# print("########## 2.2.5 ##########")
year = int(input("Please type in a year:"))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("That year is a leap year.")
elif year % 4 == 0 and year % 100 == 0:
    print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")


# print("########## 2.2.6 ##########")
letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")
if letter1 < letter2 and letter2 < letter3:
    print("The middle letter is", letter2)
elif letter2 < letter1 and letter1 < letter3:
    print("The middle letter is", letter1)
else:
    print("The middle letter is", letter3)