# Simple Python Calculator

print("--- Simple Python Calculator ---")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()

    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
            result = "Undefined"
    else:
        print("Error: Invalid operation.")

    if result is not None and result != "Undefined":
        print(f"Result: {num1} {operation} {num2} = {result}")
    elif result == "Undefined":
        print(f"Result: {num1} {operation} {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print(f"Unexpected error: {e}")

print("--- Calculator session ended ---")
