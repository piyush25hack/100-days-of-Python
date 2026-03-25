print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you wants? S, M, L: ")
pepperoni = input("Do you want pepproni on your pizz? Y or N:")
extra_cheese =input("Do you want extra cheese? Y or N:")
bill=0
# Main Program
if size == "S":
    bill=15
    print("Small Pizza Rs 15") 
elif size == "M":
    bill=20
    print("Small Pizza Rs 20")
else:
    bill=25
    print("Large Pizza Rs 25")
# Pepproni Logic
    if pepperoni== "Y":
        if size == "S":
          bill+=2
    else:
        bill+=3
# Cheese Logic
if extra_cheese == "Y":
    bill+=1
    print(f"Your Final Bill Amount is $ {bill}")