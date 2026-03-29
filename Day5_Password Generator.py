import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['!','#','$','%','&','(',')','*','+']
numbers=['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password=""

for char in range (0, nr_letters):
   password+=random.choice(letter)
for char in range (0, nr_symbols):
   password+=random.choice(symbols)
for char in range (0, nr_numbers):
   password+=random.choice(numbers)

print(password)

