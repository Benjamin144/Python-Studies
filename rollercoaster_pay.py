print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0  # Global bill

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 3
        print("Child tickets are £5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7.")
    else:
        bill = 12
        print("Adult tickets are £12.")

    photo_opp = input("Do you want a photo taken? Y or N\n")
    if photo_opp == "Y":
        bill += 3  # Local bill

    # This print statement will occur after the if statement for the photo_opp variable has been implemented
    message = (f"Your final bill is {bill}")
    print(message)
else:
    print("Sorry,you hve to grow tller before you can ride.")
