from tkinter.tix import ExFileSelectBox
from urllib import response


valid = False
while not valid:

    response = float(input("Enter a number: "))
    
    if response > 0:
        valid = True

    else:
        print("Please enter a number that is more than zero")
        print()