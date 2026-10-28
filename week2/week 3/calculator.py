class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

def main():
    calculator = Calculator()

    print("--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = input("Choose an operation (1-4): ").strip()

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice.")
            return
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = calculator.add(num1, num2)
        elif choice == "2":
            result = calculator.subtract(num1, num2)
        elif choice == "3":
            result = calculator.multiply(num1, num2)
        else:
            result = calculator.divide(num1, num2)

        print(f"Result: {result:g}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError as error:
        print(error)

if __name__ == "__main__":
    main()
