print("Welcome to the tip calculator!")

total_bill = input ("what was the total bill? ")
total_bill_as_int = int(total_bill)
percentage_tip = input("What percentage tip would you like to give 10, 12, or 15? ")
percentage_tip_as_int = int(percentage_tip)
split_bill = input("How many people to split the bill? ")
split_bill_as_int = int(split_bill)

payable = percentage_tip_as_int / 100 * total_bill_as_int / split_bill_as_int
# payable = total_bill_as_int * 100 / percentage_tip_as_int
print(payable)


total_bill_as_int 
percentage_tip_as_int 
split_bill_as_int 

