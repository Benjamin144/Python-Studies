import locale
import decimal
print("Welcome to the tip calculator!")

total_bill = input ("what was the total bill? ")
total_bill_as_int = int(total_bill)
percentage_tip = input("What percentage tip would you like to give 10, 12, or 15? ")
percentage_tip_as_int = int(percentage_tip)
split_bill = input("How many people to split the bill? ")
split_bill_as_int = int(split_bill)

payable = percentage_tip_as_int / 100 * total_bill_as_int / split_bill_as_int + total_bill_as_int
final_bill = payable / split_bill_as_int
message = (f"Each person should pay: £{final_bill:.2f}")
print(message)


