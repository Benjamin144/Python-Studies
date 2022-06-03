year = int(input("Which year would you like to check?\n:"))

def is_a_leapyear(year):
    leap = False

    # Logic
    if year%400 == 0:
        leap = true
    elif year%4 == 0 and year%100 !=0:
        leap = True
    return leap

print(is_a_leapyear(year))
