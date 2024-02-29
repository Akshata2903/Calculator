while True:
    print("Enter the operation you want to perform: +, -, *, / (or type 'exit' to quit)")
    operator = input().strip()

    if operator.lower() == 'exit':
        print("Exiting the calculator.!")
        break

    print("Enter First Number:")
    num1 = float(input())
    print("Enter Second Number:")
    num2 = float(input())

    if operator == "+":
        result = num1 + num2
        print("Addition = ", result)
    elif operator == "-":
        result = num1 - num2
        print("Subtraction = ", result)
    elif operator == "*":
        result = num1 * num2
        print("Multiplication = ", result)
    elif operator == "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Division = ", result)
    else:
        print(f"{operator} is Invalid")
