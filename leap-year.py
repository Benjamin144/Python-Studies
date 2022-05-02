year = int(input("Which year would you like to check?"))

if year / 4:
    print("This is a leap year.")
elif year / 100:
    print("This is not a leap year")
elif year / 400:
    print("This is a leap year")
else:
    print("This is not a leap Year")