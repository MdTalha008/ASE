class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            print("Invalid input: both arguments must be numbers.")
            return None

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Cannot divide by zero.")
            return None
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    x, y = 10, 5
    print("Addition:", calc.add(x, y))
    print("Subtraction:", calc.subtract(x, y))
    print("Multiplication:", calc.multiply(x, y))
    print("Division:", calc.divide(x, y))
