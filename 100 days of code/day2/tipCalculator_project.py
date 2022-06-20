"""This project is about building a tip calculator app by prompting the user to enter the total tip, the display a bill for each of the members
taking into account the tip"""


print("Welcome to the tip Calculator")

bill_amount = float(input("What was the total bill? "))
tip_amount = int(input("What percentage tip would you like yo give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

total_bill = (bill_amount *(tip_amount/ 100)) + bill_amount
each_bill = round((total_bill/num_people), 2)

print(f"Each person should pay: ${each_bill}")