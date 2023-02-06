def calculate(a, b, operation):
    if operation == "+":
        answer = a + b
    elif operation == "-":
        answer = a - b
    elif operation == "*":
        answer = a * b
    elif operation == "/":
        answer = a / b
    else:
        return "Invalid operation"
    
    return f"{a} {operation} {b} = {answer}"

def run_calculator():
    operations = {"A": "+", "B": "-", "C": "*", "D": "/"}
    print("Press A to Add")
    print("Press B to Subtract")
    print("Press C to Multiply")
    print("Press D to Divide")
    print("Press Q to Quit")

    while True:
        choice = input("Select your choice: ").upper()
        if choice == "Q":
            print("Program closed")
            break
        
        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue
        
        operation = operations[choice]
        a = int(input("First number: "))
        b = int(input("Second number: "))
        result = calculate(a, b, operation)
        print(result)

run_calculator()
