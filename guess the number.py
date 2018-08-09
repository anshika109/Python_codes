# GUESS THE NUMBER
import random
x=random.randrange(1,20)
print(x)
n=int(input("enter the number entered by user"))
if(n<x):
    print("your number is too short")
elif(n>x):
        print("your number entered is too high")
elif(n==x):
            print("your guess is true")
