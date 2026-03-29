# import random
# # randominteger = random.randint(1,10)
# # print(randominteger)

# # rand = random.random() *80
# # print(rand) 

# # rand_float = random.uniform(1,10)
# # print( round(rand_float))

# # rand= random.randint(0,1)
# # if rand ==0:
# #     print("Head")
# # else:
# #     print("tail")


# Name =["James", "Jordan", "Edward", "Robert"]


# # add or extent list 
# # Name.append("Piyush")

# rand= random.choice(Name)
# print(rand)

# # 2nd Option
# rand2 = random.randint(0,3)
# print(Name[rand2])

# vegetables = ["Potato", "Cauliflower", "Spinach" , "Brinjal" , "Tomato"]
# fruit =["Grapes", "Orange", "Mango", "Apple" , "Banana", "Kiwi"]

# food =[vegetables, fruit]
# print(food)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])