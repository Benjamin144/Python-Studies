num_char = len(input("What is your name?"))
print("Your name has " + num_chr +  "characters in it.")
print(type(num_char))

# Using the type function allows the coder to understand the object type "num_char" because the object type has not yet been defined, resulting in a name error.
# This snippet of code fails because the object has not been converted to a string and cannot be concatenated.