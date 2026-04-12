logo= '''     
        ________
       / _____ /|
      / /_____/ |
     /_______/  |
     |       |  |
     |       |  |
     |_______| /
        ||   ||
        ||   ||
        ||   ||
        ||   ||
        ||   ||
       /||   ||\
      /_||___||_\ '''
print (logo)

#Function for finding the highest bidder

def highest_bid(bidding_dictionary):
      Winner = ""
      high_bid =0
      for bidder in bidding_dictionary:
            bid_amount = bidding_dictionary[bidder]
            if bid_amount> high_bid:
                  high_bid = bid_amount
                  Winner = bidder
      print (f"The Winner is {Winner} with a bid of ${high_bid} ")


bids= {} #this is used to kept and keep updating
continue_bidding = True
while continue_bidding:
      name= input("What is your name? :")
      price = int(input("What is your bid? : $ "))
      bids [name]= price
      should_continue = input("Are there any other bidders ?  Type 'Yes' or 'No'. \n").lower()
      if should_continue == "no":
            continue_bidding=  "False"
            highest_bid(bids)
      elif should_continue == "yes":
            print("\n" *100)