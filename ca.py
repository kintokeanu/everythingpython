def add_num(a, b):
    ans = a + b
    print(str(a), "+", str(b), "=", str(ans))
    
def sub_num(a, b):
    ans = a - b
    print(str(a), "-", str(b), "=", str(ans))

def div_num(a, b):
    ans = a / b
    print(str(a), "-", str(b), "=", str(ans))

    
def mul_num(a, b):
    ans = a * b
    print(str(a), "-", str(b), "=", str(ans))
    

print("select choice")
print("press A to add")
print("press B to subtract")
print("press C to multiply")
print("press D to divide")

while True:

    choice = input("Select choice: ").lower

    if choice == 'A' or choice == 'a':
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add_num(a,b)
        
    elif choice == 'B' or choice == 'b':
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub_num(a,b)
    elif choice == 'C' or choice == 'c':
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul_num(a,b)
    elif choice == 'D' or choice == 'd':
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter secosnd number: "))
        div_num(a,b)



