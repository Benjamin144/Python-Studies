height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = float(weight)/float(height) ** 2
bmi_guage = 35
bmi_guage_int = int(bmi_guage)
bmi_as_int = int(bmi)
if bmi_guage >= 18.5:
    print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
    # if bmi_as_int < 18.5:
    #     print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
    # elif bmi_as_int > 25: 
    #     print(f"Your BMI is {bmi_as_int}, you are slightly overweight")
    # elif bmi_as_int > 30:
    #     print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_as_int} you are clinically obese.")



