name = input("What is your name? ")
print(name)


# Swap variable excercise
# The key to solving this excercise is to create a 3rd variable, because we need some temporary store.

a = input("a: ")
b = input("b: ")

c = a  # The value of 'a'condition that is an input "a", was changed and referenced in "c" and also stored in "c"
a = b  # The value that was stored in "a" is now the value of "b"
b = c  # Now the value "b" has replaced the value stored in 'c' and has become the 'new face of' the value stored in "c"


print("a: " + a)
print("b: " + b)

# Therefore the original state of each value has changed positionally and condiionally
# Also remember that when reading expressions in python conider reading them from right to left to understand the meaning of the operand


myint = 7
print(myint)

# To define a floating point number, you may use one of the following notations:

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
