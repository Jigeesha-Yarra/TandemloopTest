class Calculator:
    def __init__(self, a, b, operation):
        self.a = int(a)
        self.b = int(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            return self.a / self.b
        else:
            return "Invalid operation"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation like (add / subtract / multiply / divide): ")

calc = Calculator(a, b, operation)
result = calc.calculate()
print(result)
