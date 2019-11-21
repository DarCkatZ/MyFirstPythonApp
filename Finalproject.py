import random
from tkinter import *
randomnumber = random.randint(10000, 99999)

def callback():
    randomnumber = random.randint(10000, 99999)
    print(randomnumber)
    
window = Tk()
window.title("random number tweeter")
button = Button(window, text="Click to tweet random number", command=callback, bg = "#FA7EFF")