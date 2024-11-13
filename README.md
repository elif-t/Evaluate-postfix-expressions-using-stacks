# Evaluate-postfix-expressions-using-stacks

In this exercise, you will write a function, evaluate_postfix(expression), to evaluate a mathematical expression written in postfix notation (also known as Reverse Polish Notation) using a stack. The function will accept a single argument, expression, which is a string containing the postfix expression with each token separated by a space (e.g., "3 4 5 * +"). The function should return an integer representing the result of evaluating the expression.

In postfix notation, every operator follows all of its operands. This format eliminates the need for parentheses since the order of operations is dictated by the placement of operators. Here are some examples to illustrate:

1. Expression: "6 3 /"
    a. Apply division to 6 and 3: 6 / 3 = 2
    Result: 2

2. Expression: "3 4 5 * +"
    a. Multiply 4 and 5: 4 * 5 = 20
    b. Add 3 and 20: 3 + 20 = 23
    Result: 23

3. Expression: "3 4 + 5 *"
    a. Add 3 and 4: 3 + 4 = 7
    b. Multiply 7 and 5: 7 * 5 = 35
    Result: 35

4. Expression: "7 8 + 3 2 + /"
    a. Add 7 and 8: 7 + 8 = 15
    b. Add 3 and 2: 3 + 2 = 5
    c. Divide 15 by 5: 15 // 5 = 3 (integer division)
    Result: 3

To implement the evaluate_postfix(expression) function, follow these steps:

1. Process each token in the expression from left to right.
2. If the token is a number (operand), push it onto the stack.
3. If the token is an operator (+, -, *, /):
    a. Pop the necessary operands from the stack.
    b. Apply the operator to these operands.
    c. Push the result back onto the stack.
4. At the end of the expression, the stack should contain a single element, which is the result of the expression.

Assumptions:
- The expression is valid and contains only single-digit non-negative integers and the operators +, -, *, and /.
- Division should be integer division (use // in Python).

Test your implementation with the provided print-function.
