print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12: # if they are under 12 then....
        print("Please pay £5.")
    elif age <= 18: # are they over 18 then? elif (else if could you also check that the following condition is true)
        print("Please pay £7.")
    else: # else if they are not under 12 and over 18 then the following condtion is true
        print("Please pay £12.")
    
else:
    print("Sorry, you have to grow taller before you can ride.")

# additional conditional operators

# == Equal to
# != Not equal to
# >= Greater than or equal to
# <= Less than or equal to