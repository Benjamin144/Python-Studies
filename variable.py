a = input("a: ")
b = input("b: ")

c = a # The same value that is input "a" is now referenced in "c" and also stored there in "c"
a = b # The value that is "a" is now the value of "b"
b = c # Now "b" has now become the value stored in "c"

print("a: " + a)
print("b: " + b)

# Swap variable excercise