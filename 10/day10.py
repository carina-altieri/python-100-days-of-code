# Calculator project

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    accumulate = True

    first_number = float(input("Type the first number: "))
    while accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("Type the next number: "))
        answer = operations[operation_symbol](first_number, next_number)
        print(f"{first_number} {operation_symbol} {next_number} = {answer}")

        should_continue = input(f"Do you want to continue working with the previous result? Type 'y' to continue with {answer} or 'n' to start a new calculation: ")
        if should_continue == "y":
            first_number = answer
        else:
            accumulate = False
            print("\n" * 20)
            calculator()

calculator()



