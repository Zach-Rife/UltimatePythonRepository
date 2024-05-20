Amount_Due = 2
print("Amount due:", Amount_Due)
insert = int(input("Insert coin: "))
def vending(Amount_Due, insert):
    while Amount_Due > 0:
        if insert == 5:
            Amount_Due = Amount_Due - 5
            return Amount_Due

        elif insert == 10:
            Amount_Due = Amount_Due - 10
            return Amount_Due
        elif insert == 25:
            Amount_Due = Amount_Due - 25
            return Amount_Due
        else:
            print("Error - this coin type cannot be accepted")
    if Amount_Due < 0:
        return Amount_Due == (Amount_Due * -1)
print(vending(Amount_Due, insert))


            
    