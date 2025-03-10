# calculator.py (User A's Code)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
else:
    print("Invalid choice!")
