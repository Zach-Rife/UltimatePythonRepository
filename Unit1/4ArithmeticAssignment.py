print("########## 1.4.1 ##########")
number = int(input("Please type in a number"))
print(number, "times 5 is", number * 5)

print("########## 1.4.2 ##########")
name = input("what is yuor name?")
yearborn = int(input("which year were you born?"))
age = 2024 - yearborn
print("Hi", name, "you will be ", age, "years old at the end of the year 2024")

print("########## 1.4.3 ##########")
day = int(input("how many days?"))
seconds = day * 24 * 60 * 60 
print("Seconds in that day", seconds)

print("########## 1.4.4 ##########")
# Fix the code
number1 = int(input("Please type in the first number: ")) 
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1 * number2 * number3

print("The product is", product)

print("########## 1.4.5 ##########")
number1 = int(input("Number1:"))
number2 = int(input("Number2:"))
sum = number1 + number2
product = number1 * number2
print("The sum of the numbers:" ,sum)
print("The product of the numbers:" ,product)

print("########## 1.4.6 ##########")
number1 = int(input("Number1:"))
number2 = int(input("Number2:"))
number3 = int(input("Number3:"))
number4 = int(input("Number4:"))
sum = number1 + number2 + number3 + number4
mean = sum/4
print("The sum of the numbers is" ,sum, "and the mean is" ,mean)

print("########## 1.4.7 ##########")
schoolcafe = int(input("How many times a week do you eat at the student cafeteria?"))
priceofschool = float(input("The price of a typical student lunch?"))
grocerycost = float(input("How much money do you spend on groceries in a week?"))
daily = schoolcafe * priceofschool + grocerycost 
truedaily = daily/7
weekly = schoolcafe * priceofschool + grocerycost
print("Average food expenditure:")
print("Daily:", truedaily )
print("Weekly:", weekly)

print("########## 1.4.8 ##########")
coursesize = int(input("How many students on the course?"))
desiredgroupsize = int(input("Desired group size?"))
groupsformed = coursesize// desiredgroupsize
print("Number of groups formed:",groupsformed)