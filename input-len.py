# name = input("What is your name?" + " ")
# print(len(name))

# Cleaner alternative method
# print(len(input("What is your name? ")))

#elaboration on original method using an extra variable

# name = input("What is your name? ")
# length = len(name)
# print(length)

# Determining positonal length of a string by subscripting
# Subcripting starts from [0] or zero not 1
#string
# print("hello"[4])

# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

nu_char = len(input("What is your name "))
new_nu_char = str(nu_char)
print("Your name has " + new_nu_char + " characters, ")