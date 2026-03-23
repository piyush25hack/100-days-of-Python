print("Welcome to the tip calculator!")
bill = float(input("what is the total bill? $"))
tip = int(input("What percentage tip would you like to give ? 10 12 15 "))
people = int(input("how many people to split the bill? "))
bill_tip = tip /100 
total_amount = bill * bill_tip
total_bill = bill + total_amount
bill_pp = total_bill / people
f_amount=round(bill_pp,2)
print(f"Each Person should pay${f_amount}")