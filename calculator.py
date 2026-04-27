# Smart CLI calculator



def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Welcome to Smart Calculator")

    while True:
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using Smart Calculator, BYE 👋👋")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except:
            print("Invalid input, try again.")
            continue

        if choice == "1":
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            print(f"Result: {sub(a, b)}")
        elif choice == "3":
            print(f"Result: {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {divide(a, b)}")
        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    calculator()
