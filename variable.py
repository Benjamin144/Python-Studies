a = input("a: ")
b = input("b: ")

c = a # The value of 'a'condition that is an input "a", was changed and referenced in "c" and also stored in "c"
a = b # The value that was stored in "a" is now the value of "b"
b = c # Now the value "b" has replaced the value stored in 'c' and has become the 'new face of' the value stored in "c"

# Therefore the original state of each value has changed positionally and condiionally
# Also remember that when reading expressions in python conider reading them from right to left to understand the meaning of the operand

print("a: " + a)
print("b: " + b)

# Swap variable excercise