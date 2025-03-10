# calculator.py (User B's Code)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (3 or 4): ")

if choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice!")
