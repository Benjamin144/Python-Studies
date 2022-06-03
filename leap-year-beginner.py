print('Find out if an Earth year is a Leap year!')
year = int(input('So what Earth year would you like to check...?\n:'))
if year % 4 == 0 and year % 100 != 0:
    leap_year = True
elif year % 100 == 0 and year % 400 == 0:
    leap_year = True
else:
    leap_year = False     

message = (f"... So would the Earth year that you entered be a Leap Year? Lets find out!: {leap_year:}")
print(message)  
         
        


