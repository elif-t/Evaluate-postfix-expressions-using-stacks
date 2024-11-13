def evaluate_postfix(expression):
    # Initialize an empty stack to store operands
    stack = []
    # Split the input expression into individual tokens (operands and operators)
    tokens = expression.split()
    # Process each token in the postfix expression
    for token in tokens:
        # Check if the token is a number
        if token.isdigit():
            # Convert the token to an integer and push it onto the stack
            stack.append(int(token))
        # If the token is an operator (+, -, *, /)
        else:  
            # Pop the top two elements from the stack to use as operands
            b = stack.pop()  # Second operand (right side of the operation)
            a = stack.pop()  # First operand (left side of the operation)
            
            # Apply the operator to the two operands and push the result back onto the stack
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a // b  # Perform integer division
            stack.append(result)
    # The final result should be the only item left in the stack, so return it
    return stack[0]

# Test cases
print(evaluate_postfix("7 2 3 * - 4 +"))  # Expected output: 3
print(evaluate_postfix("2 3 1 * + 9 -"))  # Expected output: -4
print(evaluate_postfix("6 2 / 3 4 * +"))  # Expected output: 14
print(evaluate_postfix("5 9 8 + 4 * 6 - +"))  # Expected output: 75
print(evaluate_postfix("4 2 + 3 5 1 - * +"))  # Expected output: 18
