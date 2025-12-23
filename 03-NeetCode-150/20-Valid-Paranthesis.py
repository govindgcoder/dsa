"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Solution plan:
Can easily be solved using a stack.

Pseudocode:
create an empty stack
loop through each character
	if an opening paranthesis is detected, push it to the stack.
	if a closing paranthesis is detected, pop from the stack and compare if it is equal, if not return false.
return true if stack is empty

"""

from ast import Return
from multiprocessing import Value


def valid(s):
	stk = []
	brackets = {')':'(','}':'{',']':'['}
	for i in s:
		if i in brackets:
			b = stk.pop() if stk else 'c'
			if b!=brackets[i]:
				return False
		else:
			stk.append(i)
	return not stk
	
print(valid('[(][]'))