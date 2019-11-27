# section a 
q1 read the file "jabberwocky.txt" and print its content to the screen

f = open("jabberwocky.txt", "r")
print(f.read())

#q2 read the file "austen.txt" and print the amount of lines in the file

lines = 0
for line in open("austen.txt", "r"):
    lines += 1
print(lines)

#q3 each line of the file "numbers.txt" contains a number, write a script to add up all the values in the file

total = 0
for number in open("numbers.txt", "r"):
    total += int(number)
print(total)

# section b
# q1 ask the user to enter their name and append this to a file called "register.txt"

f = open("register.txt", "a")

name = True
while name: 
    name = input("Enter your name: \n")
    f.write(name + "\n")

f.close()

for name in open("register.txt", "r"):
    print(name)

#q2 create a new file called "even.txt" that contains only the even numbers from the file "numbers.txt"

f = open("even.txt", "w")

for number in open("numbers.txt", "r"):
    number = int(number)
    if number % 2 == 0:
        f.write(str(number) + "\n")


f.close()

#q3 "secret.txt" contains a secret message. each number represent a number of the alphabet where 1 = A, 2 = B... Z = 26. work out what the secret message says

alphabet = {
        0 : "_",
        1 : "A",
        2 : "B",
        3 : "C",
        4 : "D",
        5 : "E",
        6 : "F",
        7 : "G",
        8 : "H",
        9 : "I",
        10 : "J",
        11 : "K",
        12 : "L",
        13 : "M",
        14 : "N",
        15 : "O",
        16 : "P",
        17 : "Q",
        18 : "R",
        19 : "S",
        20 : "T",
        21 : "U",
        22 : "V",
        23 : "W",
        24 : "X",
        25 : "Y",
        26 : "Z",
}

word = ""
for number in open("secret.txt", "r"):
    number = int(number)
    word = word + alphabet[number]

print(word)
