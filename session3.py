#Q1
import random 
for number in range(10):
    print(random.randint(1,10))

#Q2i loop keeps repeating until the specified number is given, which it then prints
user_guess = None
while user_guess != 7:
    user_guess = int(input("Enter a number\n"))
print("Wow lucky number 7!")

#2ii the number being guessed it a random value
import random
user_guess = None
while user_guess != 7:
    user_guess = (random.randint(1,10)) 
    print (user_guess)
print("Wow lucky number 7!")

#2iii guessing game vs comp
import random
print("\nWelcome\nYou pick and a number\nIf the number is the same as the random computer number\nYou win!\n\nGood luck ;)\n")
user_guess = None
comp_number = random.randint(1,10)
while user_guess != comp_number:
    user_guess = int(input("Enter a number:\n")) 
    comp_number = random.randint(1,10)
    print(comp_number)
print("Winner")

#Q3 round cm inputs to the nearest whole msq using math module. Divided by 10000 to change cm to msq.
import math
width = int(input("Enter the width of the rectangle in cm\n")) 
height = int(input("Enter the height of the rectangle in cm\n"))
area = (width*height) / 10000
squared = math.ceil(area)
print("The area of the rectangle is:\n" + str(squared) + "msq")

#q4
password = input("Enter Password:\n")
attempts = 0
while attempts < 2:
    if password == "qwerty123":
        print("Welcome")
        break
    else:
        print("Incorrect Password\n")
        password = input("Enter Password:\n")
    attempts += 1
    print("System Failure")

#section b q1

apple = {
    "Type" : "Bramley",
    "Price" : 0.39,
    "Colour" : "Green",
    "Offer" : True
}
print(apple)
apple["Best Before"] = "12th Jan 2020"
print(apple)
for key in apple:
    print(str(key) + " = " + str(apple[key]))
del(apple["Offer"])
print(apple)
