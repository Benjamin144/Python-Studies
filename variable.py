# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a # The same value that is input "a" is now referenced in "c" and also stored there in "c"
a = b # The value that is "a" is now the value of "b"
b = c # Now "b" has now become the value stored in "c"

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)