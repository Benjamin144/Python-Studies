""" Snippet (1) """
# Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
# The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

""" Snippet (2) """
mystring = "Don't worry about apostrophes"
print(mystring)
# There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters.

""" Snippet (3) """
# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)

""" Snippet (4) """
# the use of concatenation here
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

""" Snippet (5) """
# Assignments can be done on more than one variable "simultaneously" on the same line like this
h, t = 6, 90
print(h, t)
hello, the, world = 1, 4, 4
print(hello, the, world)

""" Snippet (6) """
# The target of this exercise is to create a string, an integer, and a floating point number.
# The string should be named mystring and should contain the word "hello".
# The floating point number should be named myfloat and should contain the number 10.0, and
# the integer should be named myint and should contain the number 20.
mystring = "hello"
myfloat = 10.0
myint = 20
# testing code for
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
# The %f formatter is used to input float values, or numbers with values after the decimal place.
# This formatter allows us to specify a number of decimal places to round the values by.
# The % d operator is used as a placeholder to specify integer values, decimals or numbers.
# It allows us to print numbers within strings or other values. The % d operator is put where the integer is to be specified.
# Floating-point numbers are converted automatically to decimal values
# The %s operator is put where the string is to be specified.
# The number of values you want to append to a string should be equivalent to the number specified in parentheses after the % operator at the end of the string value.
# The following Python code illustrates the way of performing string formatting.
# The formatting using % is similar to that of 'printf' in C programming language.
# %d – integer %f – float %s – string %x – hexadecimal %o – octal The below example describes the use of formatting using % in Python

""" Snippet (7)

Add numbers and strings to the correct lists using the "append" list method
You must add the numbers 1,2 and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
You will also have to fill in the variable second_name in the name list, using the bracket operator [].
Note that the index is zero-based, so if you want to access the second item in the list, it's index will be 1. """


numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = ["Eric"]

""" this code should write out the filled arrays and then append the
second_name in the name list (Eric) """

print(numbers[0, 1, 2])
print(strings[0, 1])
print("The second name on the name list is %s" % second_name)
