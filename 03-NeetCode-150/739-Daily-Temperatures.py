"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]


Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:	
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100


# Solution implementation plan:

30, 60, 90
0,   1,  2

answer gotta be an array of the next greater temperature days index - the current index.

First lets convert the current array to a stack, waiting to find the next greatest value.

pop each element, compare its value with the current traversing element, and append the result (index of traversing - index of popped element) while the current popped element is less than the current traversing element.

result array can be initialized with zeros to account for the case where greater temperatures is not found.

stack gotta be of indexes, so to calculate the result (difference).
"""

def dailyTemp(temp):
	n = len(temp)
	res = [0]*n
	stk = []
	for i in range(n):
		# while the stack exists and the current temperature is greater than the ones in the stack, calculate the result.
		while stk and temp[i]>temp[stk[-1]]:
			curr = stk.pop()
			res[curr] = i-curr
		#append the stack with the current element to wait for a greater value
		stk.append(i)
	return res

temp = [73,74,75,71,69,72,76,73]

print(dailyTemp(temp))