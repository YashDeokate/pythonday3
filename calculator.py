def add(a, b):
    print("Addition is:", a + b)

def sub(a, b):
    print("Subtraction is:", a - b)

def mul(a, b):
    print("Multiplication is:", a * b)

def div(a, b):
    print("Division is:", a / b)


while True:
    print("Select +, -, *, / or q to quit")
    choice = input("Enter your choice: ")

    if choice == 'q':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        add(num1, num2)
    elif choice == '-':
        sub(num1, num2)
    elif choice == '*':
        mul(num1, num2)
    elif choice == '/':
        div(num1, num2)