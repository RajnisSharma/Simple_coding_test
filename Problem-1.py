# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

# --------------------------------------------

class calculater:
    def __init__(self, a: float, b: float, op: str):
        self.a = a
        self.b = b
        self.op = op
    
    def calculate(self) -> float:
        if self.op == '+':
            return self.a + self.b
        elif self.op == '-':
            return self.a - self.b
        elif self.op == '*':
            return self.a * self.b
        elif self.op == '/':
            if self.b != 0:
                return self.a / self.b
            return ValueError("Division by zero is not allowed.")
        return ValueError("Invalid operator. Use +, -, *, or /.")
        
if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    
    calc = calculater(a, b, op)
    
result = calc.calculate()
print(f"The result of {a} {op} {b} is: {result}")


# Output:
# Enter first number: 5
# Enter second number: 5
# Enter operator (+, -, *, /): *
# The result of 5.0 * 5.0 is: 25.0