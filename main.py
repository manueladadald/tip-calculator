print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentage = tip / 100
people = int(input("How many people to split the bill? "))
total_with_tip = (bill + (bill * percentage))
bill_per_person = total_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"\nEach person should pay: £{final_amount}")
