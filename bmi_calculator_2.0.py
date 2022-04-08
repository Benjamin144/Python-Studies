height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float(weight)/float(height) ** 2
bmi_as_int = int(bmi)

if bmi_as_int < 35:
    if bmi_as_int <= 18.5:
        print(f"Your BMI is {bmi_as_int}, you are underweight")
    elif bmi_as_int <= 25:
        print(f"Your BMI is {bmi_as_int}, you are normal weight")
    elif bmi_as_int <= 30:
        print(f"Your BMI is {bmi_as_int}, you are overweight")
    elif bmi_as_int <= 35:
        print(f"Your BMI is {bmi_as_int}, you are obese")
else:
    print(f"Your BMI is {bmi_as_int} you are clinically obese.")

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# def calculate_bmi():
#     kg = int(weight_tf.get())
#     m = int(height_tf.get())/100
#     bmi = kg/(m*m)
#     bmi = round(bmi, 1)
#     bmi_index(bmi)

# def bmi_index(bmi):

#     if bmi < 18.5:
#         messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
#     elif (bmi > 18.5) and (bmi < 24.9):
#         messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
#     elif (bmi > 24.9) and (bmi < 29.9):
#         messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
#     elif (bmi > 29.9):
#         messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obesity')
#     else:
#         messagebox.showerror('bmi-pythonguides', 'something went wrong!')


# bmi_guage = 35
# bmi_guage_int = int(bmi_guage)
# bmi_as_int = int(bmi)
# if bmi_guage >= 18.5:
#     print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
#     if bmi_as_int < 18.5:
#         print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
#     elif bmi_as_int > 25:
#         print(f"Your BMI is {bmi_as_int}, you are slightly overweight")
#     elif bmi_as_int > 30:
#         print(f"Your BMI is {bmi_as_int}, you are obese.")
# else:
#     print(f"Your BMI is {bmi_as_int} you are clinically obese.")
