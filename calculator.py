import re

class Calculator:
    
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

    def evaluate_expression(self, expression):
        tokens = re.findall(r'[+/*-]|\d+', expression)
        operands = []
        operators = []
        # avoid invalid expression like "3+8*/8"
        flag = 1

        
        def perform_operation():
            operator = operators.pop()
            operand2 = operands.pop()
            operand1 = operands.pop()
            if operator == '+':
                result = self.add(operand1, operand2)
            elif operator == '-':
                result = self.subtract(operand1, operand2)
            elif operator == '*':
                result = self.multiply(operand1, operand2)
            elif operator == '/':
                result = self.divide(operand1, operand2)
            operands.append(result)

        for token in tokens:
           
            if token.isdigit() and flag:
                operands.append(float(token))
                flag = 0
            elif token in ['+', '-', '*', '/'] and not flag:
                while operators and operators[-1] in ['*', '/']:
                    perform_operation()
                operators.append(token)
                flag = 1
            else:
                raise ValueError
            
            
        while operators:
            perform_operation()


        return operands[0]