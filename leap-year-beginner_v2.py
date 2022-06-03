print('Hello Folks, Lets find out if an Earth year is a leap year....\n')
print('Now lets begin....')
year =  int(input("Enter any Earth year please:\n"))
if year % 4 == 0 and year % 100 != 0:
    leap_year = True
    print("This is a leap year")
elif year % 100 and year % 400 != 0:
    print("This is a leap year")
    leap_year = True
else:
    leap_year = False
    print("This is not a leap year") 