def scrable_score(word):
    total = 0
    for letter in word:
        if letter == "a" or "e" or "i" or "o" or "u" or "l" or "n" or "s" or "t" or "r":
            total = total + 1
        elif letter == "d" or "c":
            total = total + 2
        elif letter == "b" or "c" or "m" or "p":
            total = total + 3
        elif letter == "f"or "h" or "v" or "w" or "y":
            total = total + 4
        elif letter == "k":
            total = total + 5
        elif letter == "j" or  "x":
            total = total + 8
        elif letter == "q" or "z":
            total = total + 10
print(scrable_score("hello"))

            
