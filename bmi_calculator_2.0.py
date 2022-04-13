height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight)/(height) ** 2
bmi_as_int = int(round(bmi, 2))

if bmi_as_int < 35:
    if bmi_as_int <= 18.5:
        print(f"Your BMI is {bmi_as_int}, you are \033[1munderweight")
    elif bmi_as_int <= 25:
        print(f"Your BMI is {bmi_as_int}, you are \033[1mnormal weight")
    elif bmi_as_int <= 30:
        print(f"Your BMI is {bmi_as_int}, you are \033[1moverweight")
    elif bmi_as_int <= 35:
        print(f"Your BMI is {bmi_as_int}, you are \033[1mobese")
else:
    print(f"Your BMI is {bmi_as_int} you are \033[1mclinically obese.")

    # total_usd = round(euro * usd, 2)

#     bmi = (weight)/(height) ** 2
# bmi_as_int = int(round(bmi, 2))

# if bmi_as_int < 35:
#     if bmi_as_int <= 18.5:
#         print(f"Your BMI is {bmi_as_int}, you are \033[1munderweight")
#     elif bmi_as_int <= 25:
#         print(f"Your BMI is {bmi_as_int}, you are \033[1mnormal weight")
#     elif bmi_as_int <= 30:
#         print(f"Your BMI is {bmi_as_int}, you are \033[1moverweight")
#     elif bmi_as_int <= 35:
#         print(f"Your BMI is {bmi_as_int}, you are \033[1mobese")
# else:
#     print(f"Your BMI is {bmi_as_int} you are \033[1mclinically obese.")
