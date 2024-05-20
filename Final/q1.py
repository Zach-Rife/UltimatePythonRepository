fname = input("Please enter  first name:")
lname = input("Please enter last name: ")
GPA = float(input("Please enter a gpa: "))
lastname = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m" "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
day = " "
scholarship = 0
if lname[0] > "k":
    day = "Tuesday and Friday."
else:
    day = "Monday and Thursday."
if GPA < 3.25:
    scholarship = 0
elif GPA < 3.5:
    scholarship = 4000
elif GPA < 3.7:
    scholarship = 8000
elif GPA < 3.86:
    scholarship = 12000
else:
    scholarship = 16000
print("Hello,", fname, "You should report to school on", day, "You are eligable for a scholarship of", scholarship)
