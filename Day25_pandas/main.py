# import csv
# import os
# import pandas as pd
# content = pd.read_csv("weather_data.csv")
# print(content[content.temp == content.temp.max()])


import pandas as pd

data = pd.read_csv("Census.csv")

# Filter the data first, then take the length
grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(grey)
print(red)
print(black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, red, black]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")