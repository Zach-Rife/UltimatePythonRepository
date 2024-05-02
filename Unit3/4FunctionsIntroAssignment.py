# ========== 3.4.1 ==========
def seven_dwarves():
    print("Bashful")
    print("Doc")
    print("Dopey")
    print("Grumpy")
    print("Happy")
    print("Sleepy")
    print("Sneezy")
seven_dwarves()

# ========== 3.4.2 ==========
def first_character():
    print("python"[0:1])
    print("yellow"[0:1])
    print("tomorrow"[0:1])
    print("heliotrope"[0:1])
    print("open"[0:1])
    print("night"[0:1])
first_character()

# ========== 3.4.3 ==========
def mean(n1, n2, n3):
    print("mean is", (n1+n2+n3)/3)
mean(5, 3, 1)
mean(10, 1, 1)
# ========== 3.4.4 ==========
def print_many_times(text, num):
    while True:
      print(text)
      num = num - 1
      if num == 0:
         break
numb = int(input("Number:"))
print_many_times(numb)



# ========== 3.4.5 ==========
def hash_square(length):
    total = 0 
    while True:
        print("#" * length)
        total = total + 1
        if total == length:
            break
numb = int(input("Number:"))
hash_square(numb)

# ========== 3.4.6 ==========
def chessboard(length):
    total = 0
    while True:
        if length % 2 == 0:
            print("10" * (length//2))
            print("01" * (length//2))
            total = total + 1
            if total == (length//2):
                break
        else:
            print("10" * (length//2) + "1")
            print("01" * (length//2) + "0")
            total = total + 1
            if total == (length//2):
                break
numb = int(input("Number:"))
chessboard(numb)

