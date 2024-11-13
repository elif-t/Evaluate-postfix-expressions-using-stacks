def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  # If it's a number, push to stack
            stack.append(int(token))
        else:  # Otherwise, it's an operator
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
    
    return stack.pop()

print(f'''{evaluate_postfix("7 2 3 * - 4 +")}
{evaluate_postfix("2 3 1 * + 9 -")}
{evaluate_postfix("6 2 / 3 4 * +")}
{evaluate_postfix("5 9 8 + 4 * 6 - +")}
{evaluate_postfix("4 2 + 3 5 1 - * +")}
{evaluate_postfix("8 3 1 - 3 * + 6 2 / +")}''')
