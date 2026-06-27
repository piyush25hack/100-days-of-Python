# Error Handling
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found! Creating new...")
    data = {}
except KeyError as error:
    print(f"Key {error} not found!")
else:
    print("File loaded successfully!")
finally:
    print("Operation complete!")

# JSON Read/Write
import json

# Write
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read
with open("data.json", "r") as file:
    data = json.load(file)