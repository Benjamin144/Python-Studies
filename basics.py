# coding exercise 1.1
#print('Day 1 - Python Print Function\nThe function is declared like this:\nprint("what to print")')

# coding exercise 1.2
#print ("Hello" + " " + "Joe")
# print("Day 1 - String Manipulation")
# print('String Concatenation is done with the "+" sign.')
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")

# input prerequisites
# input() will get user in console
# then print () will print the word "Hello" and the user input
# print("Hello " + input("what is your name?"))

# coding exercise 1.3
# print( len( input ("What is your name?") ) )

# variable prerequisites
# name = "Jake"
# print(name)

# name = "Benjamin"
# print(name)

# name = input("What is your name?")
# length = len(name)
# print(length)

# coding exercise 1.4
# a = input("a: ")
# b = input("b: ")

# Attempt 1 (Tuple swap without variables) 
# a, b = b, a 
# or

# Attempt 2 (Temporary variable)
# c = a
# a = b
# b = c

# Attempt 3 (Arithmetic operators - - broken code)
# a = ("a: ")
# b = ("b: ")

# a = a + b # a = 44, b = 22
# b = a - b # a = 44, b = 22
# a = a - b # a = 22, b = 44


# print("a: " + a)
# print("b: " + b)

# Datatypes

#string
# print("hello"[4])

# print("123" + "345") # concatenates strings within parentheses

# new_num_chr = str(num_char)
# print("Your name contains " + new_num_char + characters")

#  Integer

# print(123 + 345) # Adds two integers together

# 134_265_4896

#Float

# 3.14159
# a = float(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70)+ str(100))

# Boolean

# True
# False

# coding exercise 1.2 (Final)
# two_digit_number = input("Type a two digit number: ") 
# num1 = int(two_digit_number[0]) #Gets the first and second digits using subscripting and then converts each string to an integer
# num2 = int(two_digit_number[1]) #Gets the first and second digits using subscripting and then converts each string to an integer
# total = (num1) + (num2) # Adds the two digit nuber together without concatention because of string conversion
# print(total)

# Mathematical operations in Python

# 3 + 5
# 7 - 6
# 4 * 5
# print(10 /5) # When divide Python will always convert the mathematical operation to a float
# print(type(10 /5)) # for example the type command identifies this
# print(2 ** 2)
# print(2 ** 3)
# print(2 ** 4)
# print(2 ** 5)
# print(2 ** 6)
# print(2 ** 7)
# print(2 ** 8)
# print(2 ** 9)
# print(2 ** 10)
# z = 2 - 6.1j
# print(type(z))

# Python uses PEMDAS (the priority of mathmatical operations)
# Parenthesis = ()
# Exponents = **
# Multiplication = *
# Division = /
# Addition = +
# Subtraction = -
# (Left)
# (Right)

# Because of the order pf priority the PEMDAS method can look decieving because the IMPORTANCE of operation below are the same
# ()
# **
# * / # However the operation most to the left will be prioritised or sequenced between multiplicaton and division
# + -

# Therefore: PEMDASLR (LR - left/right)
# print(3*3+3/3-3)
# print(type(3 * 3 + 3 / 3 - 3)) # 3*3 and 3/3 are of equal importance, but the calculation goes from left to right in order of sequence
# print(3*3/3+3-3) # Here you can use parenthesis() to isolate bits of code that have lower priority in terms of PEMDASLR and therefore turn them into higher priority operations
# # Or:
# print (3*(3+3)/3-3)


# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# total = (num1) + (num2)
# print(total)

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# bmi = float(weight) / float(height) ** 2
# BMI = int(bmi)
# print(BMI)

# Code researched for this program to work
# # bmi = float(height) / int(weight)
# bmi = weight / (height ** 2)
# BMI = round(bmi)

# print(bmi)

# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)
# #PEMDSR
# bmi = weight / (height ** 2)
# BMI = round(bmi)

# Number Manipulation & "F" Strings in Python
print(8 / 3) # outputs a floating point number
print(int(8 / 3)) # output of int chops off floating numbers
print(round(8 / 3)) # makes the number an integer from a floating point number depending on the calculation being clean
print(round(8 / 3, 2)) # specifiys the precision of the number of digits rounded to.
print(round(2.666666666666, 2)) # alternativley, it can be written like this.
# another way of dividing numbers is to use the floor division //
print (8 // 3)
# in Python a number divided by a number outputs a floating point number 
# If you didn't need a FPN then the floor division would chop the FPN's off without converting it into an integer.
print(type(8 // 3)) # Integer
print(type(8 / 3)) # Float
print(type(4 / 2)) # Float even with a clean division
print (4 / 2) # as represented here
# if we save the results of this calculation into a variable
result = 4 / 2
# you can then continue to do calculations on this variable
result = 4 / 2
result /= 2 # divides by 2 again
print(result)

# when writing code for example to keep track of a users score
score = 0
# User scores a point
# rather than using the previous value of score
score = score + 1
# use the short hand
score += 1
print(score)
# you can use this method in the following way, to manipulate a value based on its previous value
score -= 1
score /= 1
score *= 1

score = 0
# previously we had to use this type of code
# print("Your score is " + score) # because these are different datatypes the code will return an error
print("Your score is " + str(score)) # so we have to convert the variable into a string to debug the code
print(score)

# sometimes programmers require a more convenient way of storing differing datatypes
score = 0 # integer
height = 1.8 # float
isWinning = True # boolean
print("Your score is ") # find some way of integrating all of the above datatypes into this string
#instead of having to use all of the above data and a whole load of concatenation, then converting them into a string
print("Your score is " +str(score)) #this can be longwinded, and could break leading to alot of frustration.

#f-string
print("Your score is ")
# you type the character f infront of the string and it should go in front of the double or single quotes most importantly 
f"your score is " # this is now an f-string and I can now start adding characters in front of the f-string
# so if I wanted to write "your score is " = to the the variable score I would put the variable score inside a set of curly braces, within the string
print(f"Your Score is {score}") # so when the code is run python will convert the variables within the string in the background, without the use of concatenation and data conversion.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆



#Write your code below this line 👇
days = int(365 * 90) - 365 * int(age)
weeks = int(52 * 90) - 52 * int(age) 
months = int(12 * 90) - 12 * int(age)

print (f"You have {days} days, {weeks} weeks, and {months} months left.")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message =  (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
print(message)
