print("Hai")
def add(a,b):
    thisTot = a + b
    return thisTot
fnumber = int(input("What is the first number?"))
snumber = int(input("What is the second number?"))
total = add(fnumber, snumber)
if total >= 100 :
    print("Number is larger than 100.")
elif total < 100:
    print("This is small brain.")
if fnumber == 2 and snumber == 2:
    print("fish")
elif fnumber != 2 or snumber !=2:
    print(total)
