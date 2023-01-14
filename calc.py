def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + "+" + str(b) + "=" + str(answer))

while True:
    print("press A to Add")
    print("press B to Subtract")
    print("press C to Multiply")
    print("press D to Divide")
    print("press e to Quit")

    choice = input("select yout choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("first number: "))
        b = int(input("second number: "))
        add(a, b)

    elif choice == "b" or choice == "b":
        print("Subtraction")
        a = int(input("first number: "))
        b = int(input("second number: "))

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("first number: "))
        b = int(input("second number: "))

    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("first number: "))
        b = int(input("second number: ")) 

    elif choice == "e" or choice == "E":
        print("Program closed")
        quit()
