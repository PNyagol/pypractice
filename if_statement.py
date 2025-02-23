is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")


elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")

else:
    print("Enjoy your day")

# Test

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price

print(f"Down Payment = ${down_payment}")

# Logical Operators
#AND

high_income = True
good_credit = True

if high_income and good_credit:
    print('Eligibal for a loan')


#OR

income = True
credit = False

if income or credit:
    print('Eligibal for a loan')


#comparison operators

temperaure = 35
if temperaure > 30:
    print("It's a hot day")

else:
    print("It's not a hot day")

#Exercise

name = input("Enter Name: ")

if len(name) < 3:
    print("Name must be atleast 3 characters")

elif len(name) > 50:
    print("Name can be a maximum of 50 characters")

else:
    print("Name looks good")



# Weight Converter

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilograms")

else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


#while loop

# We use while loops to execute a block of code multiple times

# they are always useful in building interactive programs and games

# write while followed by consition and a collon
# as long as this condition is true the code on the bloack will be executed repetetively 

i = 1
while i <= 5:
    print(i)
    i += 1
print("The loop is done")

# Gessing Game Using WHile lop

secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_num:
        print("Congratulations! You Won!")
        break
else:
    print("Ooooops! You Faild")


#Car Game
command = ""
started = False

while True:
    command = input("> ").lower()
    
    if command == "start":
        if started:
            print("Please note the car is already started.")
        
        else:
            started = True

        print("Car started..")
    
    elif command == "stop":
        if not started:
            print("Car already stopped")
        
        else:
            started = False
            print("Car stopped")
    
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
              """)
    
    elif command == "quit":
        break

    else:
        print("Sorry! I do not understand this.")

# For Loops
# loop over items of a collection such as characters in a string 

for item in "Python":
    print(item)

# Lists and for loop

for item in ["Peter Nyagol", "Joan Winga", "Edwina Asha"]:
    print(item)

# Iterate over a large list of numbers

for item in range(10):
    print(item)

# start the range from a point say 5
for item in range(5, 10):
    print(item)


# start the range from a point say 5 and give it intervals or steps say 2
for item in range(5, 10, 2):
    print(item)


#calculate total of list items using a for loop

# += is called an augmented assignment operator
# hence total = total + price is UNIVERSALLY expressed as total += price

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total = {total}")

#Nested Loops
# Means adding one loop inside another loop

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


# Exercise
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('x' * number)

#Using nested loops
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
        print(output)