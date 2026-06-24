# Functions for basic mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Check to prevent division by zero errors
    if y == 0:
        return "Error! Division by zero."
    return x / y

# The main interface loop
while True:
    print("\n=== Python Calculator ===")
    print("Select an operation:")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    # Check if the user wants to exit first
    if choice == '5':
        print("Closing the calculator. Goodbye!")
        break
        
    # Check if the choice matches one of our valid operations
    if choice in ['1', '2', '3', '4']:
        # Taking input from the user and converting strings to decimals (float)
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            
    else:
        print("Invalid Input. Please select a valid option.")