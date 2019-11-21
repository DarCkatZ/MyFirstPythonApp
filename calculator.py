import tkinter
pName = input("Please, enter your name?")
print("Hello, " + pName + ".  I'm the calculating wizard. Enter your numbers and see if you can stump me...")
def calc(a,b,op):
    if op == "+":
        thisTot = a + b
    elif op == "-":
        thisTot = a - b
    elif op == "*":
        thisTot = a * b
    elif op == "/":
        thisTot = a / b
    return thisTot
fnumber = int(input(pName + ", what is your first number?  "))
snumber = int(input(pName + ", what is your second number?  "))
op = input(pName + ", now tell me what you want me to do with the numbers i.e. +, -, /, or *:  ")
total = calc(fnumber, snumber, op)
if total >= 100 :
    print(pName + ", that number is larger than 100, but still easy peesy. Calculating.... Your answer is....")
elif total < 100:
    print(pName + ", this is small brain.  Your answer is....")
if fnumber == 2 and snumber == 2:
    print("fish")
elif fnumber != 2 or snumber !=2:
    print(total)
