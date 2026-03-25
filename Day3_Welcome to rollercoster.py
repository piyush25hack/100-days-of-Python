print("Welcome to the rollercoster ride")
height = int(input("Let's Check you height first"))
bill = 0
if height >= 120:
    print("You can ride the rollercoster")
    age= int(input("Write your age please?"))
    if age<=12:
         bill= 5
         print("Child Ticket are $5")
    elif age<=18:
         bill= 7
         print("Youth Ticket are  $7")
    else:
         bill =12
         print("Adult Tickets are $12")
    want_photo = input("Do you want to take photos Type y for Yes and n for No ").lower()

if want_photo == 'y':
    bill += 3
    print(f"Your final Bill Amount $ ")
else:
    print("sorry you can't ride the rollercoster")
    
