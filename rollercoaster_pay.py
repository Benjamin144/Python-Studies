print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0  # Global bill counter

if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input('What is your age? '))
    if age < 12:  # depending on the condition the variable 'bill' will be changed to a different number.
        bill = 3  # sets bill variable to specific integer that represents £3
        print('Child tickets are £5.')
    elif age <= 18:  # depending on the condition the variable 'bill' will be changed to a different number.
        bill = 7
        # sets bill variable to specific integer that represents £7
        print('Youth tickets are £7.')
    else:
        bill = 12
        # sets bill variable to specific integer that represents £12
        print('Adult tickets are £12.')

    photo_opp = input('Do you want a photo taken? Y or N\n')
    if photo_opp == 'Y':
        bill += 3  # Local bill
    # No requirement for accompanying else statement because the program doesn't require it.

    # This print statement will occur after the if statement for the photo_opp variable has been implemented
    message = (f'Your final bill is £{bill}')
    # This print statement will happen after the above if statement has been executed.
    print(message)
else:
    print('Sorry,you have to grow taller before you can ride.')

    # When working with if else statements the indentation is key to running the program effectively
