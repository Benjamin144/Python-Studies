year = int(input("Which year would you like to check?\n:"))

def is_a_leapyear(year):
    leap = False

    # Logic
    if year%400 == 0:
        leap = true
    elif year%4 == 0 and year%100 !=0: # The % operator 'returns' the modulo (i.e. remainder) of 'a' division. 
                                       # The == operator 'compares the value or equality of two objects', 
                                       # (a%b==0) is true when a is divisible by b.
                                       # They are testing if the year is divisible by 4. 
                                       # My guess is that they are testing if it is a leap year. 
                                       # However you'd also need to add a test to see if the year is also dividible by 100 or 400.
        leap = True
    return leap

print(is_a_leapyear(year))
