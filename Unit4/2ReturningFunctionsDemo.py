# ========== 4.2.1 ==========
# def greatest_number(n1, n2, n3):
#     if n1 > n2 and n1 > n3:
#         return n1
#     elif n2 > n3:
#         return n2
#     else:
#         return n3
# n1 = int(input("number:"))
# n2 = int(input("number:"))
# n3 = int(input("number:"))
# greatest = greatest_number(n1, n2, n3)
# print("The greatest number is", greatest)


# ========== 4.2.2 ==========
def same_char(word, n1, n2):
    if word[n1] == word[n2]:
        return "True"
    else:
        return "false"
word = input("Please type in a string")
n1 = int(input("Please type in a number"))
n2 = int(input("Please type in a number"))
sameword = same_char(word, n1, n2)
print(sameword)


# ========== 4.2.3 ==========
sentence = "It was a dark and stormy python"
def first_word(sentence):
    index = 0
    sent = ""
    while True:
        if sentence[index] == " ":
            break
        else:
            sent = sent + sentence[index]
            index = index + 1
    return(sent)
first = first_word(sentence)
print(first)


sentence = "It was a dark and stormy python"
def second_word(sentence):
    first = len(first_word(sentence))
    index = 0
    sent = ""
    while True:
        if sentence[index] == " ":
            if first == index:
                index = index + 1
                sent = " "
            else:
                break
        else:
            sent = sent + sentence[index]
            index = index + 1
    return(sent)
second = second_word(sentence)
print(second)




sentence = "It was a dark and stormy python"
def first_word(sentence):
    index = len(sentence)- 1
    sent = ""
    while True:
        if sentence[index] == " ":
            break
        else:
            sent = sentence[index] + sent
            index = index -1
    return(sent)
first = first_word(sentence)
print(first)



