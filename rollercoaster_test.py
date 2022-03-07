print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12: # if they are under 12 then....
        print("Please pay £5.")
    elif age <= 17: # are they over 18 then? elif (else if could you also check that the following condition is true)
        print("Please pay £7.")
    elif age <= 19:
        print("Please pay £9.")
    else: # else if they are not under 12 and over 18 then the following condtion is true
        print("Please pay £12.")
    
else:
    print("Sorry, you have to grow taller before you can ride.")

# Wprking with conditional operators 

# == Equal to
# != Not equal to
# >= Greater than or equal to
# <= Less than or equal to
# += Addition AND
# -= Subtraction AND
# *= Multiplication AND
# Division AND
# **= Exponent AND
# %= Modulo AND
# //= Floor Division AND

