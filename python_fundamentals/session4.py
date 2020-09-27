# q1 creating a function to print my name wihtout accepting parameters

def name():
    print("graham")

name()

# q2 write a function that accepts a name parameter and prints hello, name

def hello_name(name):
    print("hello, " + name)

hello_name("graham")

# q3 looping through sepcified list using until fuction from q2

def hello_name(name):
    print("hello, " + name)

people = ["alice", "bob", "charlie"]

for person in people:
    hello_name(person)

# q4 write a function that prints the area of two passed in parameters

def area(x, y):
    print(x * y)

area(23,8)

# q5 write a function called print_list that accepts a list as a parameter

def print_list(names):
    for name in names:
        print(name)

print_list(["bob", "jackie", "rita"])

#q6 put school age code into a function

def eligibility(age):
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

eligibility(0)
eligibility(20)
eligibility(15)

# section b example - functions-returrning

def area(x,y,z):
    return x * y * z

cube1 = area(2,5,8)
cube2 = area(21,15,8)

print(cube1, cube2)

# q1 write a function that will return true if the number is odd and false if not

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

num = is_odd(13)

print(num)
    
#q2 write a function that accepts a word and returns it backwards, e.g 'hello' -> 'olleh'

def word_reverse(word):
    letter_count = len(word)

    while letter_count != 0:
        letter_count = letter_count -1
        print(word[letter_count])

word_reverse ("hello")

#q3 write a recursive that aceepts and prints that number of stars, followed by ever decreasing stars on each line.

def stars_in_row(stars):
    star = ""
    for x in range(0, stars):
        star = star + "*"
    print(star)
    if stars > 1:
        stars_in_row(stars -1)

stars_in_row (21)



#q4 create a padlock function to be able to enter a passcode and if its correct return 'unlocked', else 'locked'

def pin_number(pin):
    if pin == "gerg1":
        print("unlocked")
    else:
        print("locked")

pin_number("jerry2")
pin_number("gerg1")


