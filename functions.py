def trial_function():
    a = 2
    return a

print(trial_function())

c = 39
b = 76

if c > b:
    print(c)
else:
    print (b)


def patient_details (name, age):
    return name, age
print(patient_details("John Smith", 20))


def student_details (name, age, grade, streem):
    return f"Name: {name}, Age: {age}, Grade: {grade}, Streem: {streem}"
print(student_details("Peter Nyagol", 32, 80, "4 West"))

# Asking users for INPUT

name = input("What is your name? ")

print("Hi " + name) #this is string concatenation


#Exercise

x_name = input("What is your full name please?  ")
color = input("What is your favorite color?  ")
print(x_name + " likes " + color)


#Type Conversion : A program that asks YOB calculates our age and prints it on the terminal

yob = input("Birth Year: ")
myage = 2015 - int(yob)
print(myage)

#Weight Exercise

weight_lbs = input("how much do you weight in lbs?: ")
weight_kgs = int(weight_lbs) * 0.45
print(weight_kgs)