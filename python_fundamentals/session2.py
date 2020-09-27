#q1
name = input("what is your name? ")
if name == "Bob":
    print("Welcome Bob!")

#q2
name = input("what is your name? ")
if name != "Alice":
    print("youre not Alice!!!!")

#q3
password = input("Enter Password ")
if password == "qwerty123":
    print("You have successfully logged in")
else:
    print("Password Failure")

#q4
number = int(input("Enter number "))
if number %2 == 0:
    print("Even")
else:
    print("Odd")

#q5
number1 = int(input("give me a number\n"))
number2 = int(input("give me another number\n"))
if number1 + number2 > 21:
    print("bust")
else:
    print("safe")

#section b q1
name = input("What is your name?\n")
if name == "Alice":
    print("Hello, Alice")
elif name == "Bob":
    print("You're not Bob! I'm Bob")
else:
    print("You must be Charlie")

#q2
age = int(input("what is your age?\n"))
if age >= 1 and age < 11:
    print("you're too young for this school")
elif age >= 11 and age <= 16:
    print("you can come to this school")
elif age > 16:
    print("you're too old for this school")
elif age == 0:
    print("you're not even born!")
else:
    print("thats not a number... duh")

#q3
month = input("What month would you like me to check the season for?\n")
if month == "May" or month == "April" or month == "March":
    print(month + " is in Spring")
elif month == "December" or month == "January" or month == "February":
    print(month + " is in Winter")
elif month == "June" or month == "July" or month == "August":
    print(month + " is in Summer")
elif month == "September" or month == "October" or month == "November":
    print(month + " is in Autumn")
else: 
    print("i dont know")

#q4
number1 = int(input("give me a number\n"))
number2 = int(input("give me another number\n"))
if number1 % 2 == 0 and number2 % 2 == 0:
    print("even")
elif number1 % 2 == 1 and number2 % 2 == 1:
    print("odd")
else:
    print(number1 * number2)

#section c
fruit = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruit)
fruit.append("Grapes")
print(fruit)
fruit[2]="Strawberries"
print(fruit)
del(fruit[0])
print(fruit)
print(len(fruit))
fruit.sort()
print(fruit)

#section d
created a variable 'fruit' to print each item of fruit in the list fruities
fruities = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
for fruit in fruities:
    print(fruit)

#q2
for number in range(101):
    print(number)

#q3
for number in range(1, 101, 2):
    print(number)

#q4
for number in range(1896, 2019, 4):
     print(number)

#q5
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)