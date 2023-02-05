# Exercises: Level 1
#Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#Write a python comment saying 'Day 2: 30 Days of python programming'
#Declare a first name variable and assign a value to it
#Declare a last name variable and assign a value to it
#Declare a full name variable and assign a value to it
#Declare a country variable and assign a value to it
#Declare a city variable and assign a value to it
#Declare an age variable and assign a value to it
#Declare a year variable and assign a value to it
#Declare a variable is_married and assign a value to it
#Declare a variable is_true and assign a value to it
#Declare a variable is_light_on and assign a value to it
#Declare multiple variable on one line

# Day 2: 30 Days of python programming
firstname = "Matt"
lastname = "Trimboli"
fullname = firstname + " " + lastname
country = "US"
city = "Great Falls"
age = 53
year = 2023
is_married = True
is_true = True
is_light_on = True
number, street = "10730", "Sugar Meadow Ct"

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(number))
print(type(street))
# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
# Using the len() built-in function, find the length of your first name
# Compare the length of your first name and your last name
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
# Subtract num_two from num_one and assign the value to a variable diff
# Multiply num_two and num_one and assign the value to a variable product
# Divide num_one by num_two and assign the value to a variable division
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# Calculate num_one to the power of num_two and assign the value to a variable exp
# Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print ("First name " + firstname + " is " + str(len(firstname)) + " characters long.")
if len(firstname) > len(lastname):
    print ("First name is longer")
elif len(lastname) > len(firstname):
    print ("Last name is longer")
elif len(lastname) == len(firstname):
    print ("First name and last name are equal")


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ^ num_two
floor_division = num_one // num_two
radius = 30
area_of_circle = 3.14 * int(radius) ** 2.0
circum_of_circle = 2 * 3.14 * radius
radius = input ("radius: " )
area_of_circle = 3.14 * int(radius) ** 2
print ("area: " + str(area_of_circle))
firstname = input("first name: " )
lastname = input("last name: " )
country = input("country: " )
age = input("age: " )



