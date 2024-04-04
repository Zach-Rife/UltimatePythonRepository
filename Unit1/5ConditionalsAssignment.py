
print("########## 1.5.1 ##########")
number = int(input("Please type in a number"))

if number == 1984:
   print("Orwell")

print("########## 1.5.2 ##########")
number = int(input("Please type in a number"))
if number < 0:
   print("The absolute value of this number is", number * -1)
if number > 0:
   print("The absolute value of this number is", number)

print("########## 1.5.3 ##########")
name =input("What is your name?")
if name != "Jerry":
    soup = int(input("How many portions of soup?"))
    print("The total cost is", 5.9 * soup)

print("Next Please!")
print("########## 1.5.4 ##########")
number = int(input("Type in number"))
if number < 1000:
   print("This number is smaller than 1000")
if number < 100:
   print("This number is smaller than 100")
if number < 10:
   print("This number is smaller than 10")
print("THank you")

print("########## 1.5.5 ##########")
number1 = int(input("Number1:"))
number2 =int(input("Number1:"))
operation = input("operation:")
if operation == "add":
    print(number1,  "+", number2, "=", number2 + number1)
if operation == "subtract":
    print(number1,  "-", number2, "=", number2 - number1)
if operation == "multiply":
    print(number1,  "*", number2, "=", number2 * number1)
if operation == "divide":
    print(number1,  "/", number2, "=", number2 / number1)
print("########## 1.5.6 ##########")
temp = int(input("Type in a temperature (F)"))
print(temp, "degrees Fahrenheit equals", (temp-32) * (5/9),  "degrees Celsius" )
if temp < 32:
    print("Brr! It's cold in here!")
print("########## 1.5.7 ##########")
hourwage = float(input("Hourly wage:"))
hoursworked = int(input("Hours worked:"))
dayofweek = input("Day of the week:")
if dayofweek == "Sunday":
    print("Daily wages:", (hourwage * 2) * hoursworked)
print("Daily wages: ", hoursworked * hourwage)
print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
    print("You now have", points, "points")
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
    print("You now have", points, "points")

print("########## 1.5.9 ##########")
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature:"))
rain = input("Will it rain (yes/no)")
if temp > 20:
    print("Wear jeans and a T-shirt")
if temp <= 19:
    print("Wear jeans and a T-shirt, I recommend a sweater as well ")
if temp <= 10:
    print("Wear jeans and a T-shirt, I recommend a sweater as well, Take a jacket with you, ")
    
if rain == "yes":
    print(" Make it a warm coat, actually I think gloves are in order, Don't forget your umbrella!")