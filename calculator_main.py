<<<<<<< HEAD
# calculator.py (User A's Code)
=======
# calculator.py (User B's Code)
>>>>>>> userB
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
<<<<<<< HEAD
print("1. Add")
print("2. Subtract")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
=======
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
>>>>>>> userB
else:
    print("Invalid choice!")
