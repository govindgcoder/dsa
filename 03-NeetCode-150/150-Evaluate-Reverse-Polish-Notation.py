"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

AKA postfix evaluation

Evaluate the expression. Return an integer that represents the value of the expression.
- The valid operators are '+', '-', '*', and '/'.
> So we would need a switch case for that
- Each operand may be an integer or another expression.
> Combine the tokens ig - aka iterate through each character
- The division between two integers always truncates toward zero.
> use the int(a/b) => float division to integer conversion in python results in trunacation to zero
- There will not be any division by zero.
> ...
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
> no need to worry since python.

---

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Solution plan:
	
So a stack can be used to keep track of operands.

loop through each character in each element of the array.
Every time an operand is detected, push it to the stack after conversion to int.
Every time an operator is detected, pop two numbers from the stack and then push the result in the stack.

"""

def eval(arr):
	operands = []
	for tkn in arr:
		match tkn:
			case '+':
				b = operands.pop()
				a = operands.pop()
				operands.append(a+b)
			case '-':
				b = operands.pop()
				a = operands.pop()
				operands.append(a-b)
			case '*':
				b = operands.pop()
				a = operands.pop()
				operands.append(a*b)
			case '/':
				b = operands.pop()
				a = operands.pop()
				operands.append(int(a/b))
			case _:
				operands.append(int(tkn))
	return operands[0]	
	
	
print(eval(["4","13","5","/","+"]))