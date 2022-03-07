height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = float(weight)/float(height) ** 2
bmi_as_int = int(bmi)

if bmi_as_int <= 18:
    print(f"Your BMI is {bmi_as_int}, you are underweight.")
if bmi_as_int <= 22:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
if bmi_as_int <= 28:
    print(f"Your BMI is {bmi_as_int}, you are slightly overweight")
if bmi_as_int <= 33:
    print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_as_int} you are clinically obese.")



