def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def calculator():
    print("🔢 Welcome to the Python Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Exit")

        choice = input("Enter choice (1–7): ")

        if choice == "7":
            print("👋 Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("❌ Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            print("Result:", modulus(num1, num2))
        elif choice == "6":
            print("Result:", power(num1, num2))


if __name__ == "__main__":
    calculator()
