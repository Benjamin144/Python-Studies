# Any object which is not a string can be formatted using the %s operator as well
# The string that returns from the "repr" method of that object is formatted as the strings

# This prints out: A list: [1, 2, 3, 4]

list = [1, 2, 3, 4]
print("A list %s" % list)

starSystemsSecurity = 144
print("New Eden Security Systems %.4f" % starSystemsSecurity)

# Here are some basic argument specifiers that I should know:

# %s - String (or any object with string representation, like numbers)
# %s - Integers
# %f - Floating point numbers
# %.<number of digits>f - floating point number with a fixed amount of digits to the right of the dot.
# %x %X - integers in Hex representation (lowercase/uppercase)

# String formatting excercise

# WRONG SOLUTION
# data = ("John", "Doe", 53.44)
# format_string = "hello"
# print("%s Your current balance is %s %f " % format_string)

# CORRECT SOLUTION
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
# Hello John Doe. Your current balance is $53.44.
