logo = """
 _____________________
|  _________________  |
| | Python Calc     | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
def add (n1, n2):
    return n1+n2

def subtract (n1, n2):
    return n1-n2

def multiply (n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations ={"+": add,
          "-": subtract,
          "*": multiply,
          "/": divide}
def calculator():
    print(logo)
    should_Accumulate = True
    num1 = float(input("What is your first number?: "))
    while should_Accumulate:
        for sign in operations:
            print(sign)
    operation_symbol = input("Pick an operation:")
    num2 = float(input("what is the next number ?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'Y' to continue calculating with  {answer} or Type 'N' to start a new calculation: ").lower()

    if choice == "Y":
        num1 = answer
    else:
        should_accumulate= False
        print("\n"*100)
        calculator()
calculator()