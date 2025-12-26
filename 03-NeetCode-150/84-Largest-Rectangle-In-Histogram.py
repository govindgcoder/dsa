"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.

Input: heights = [7,1,7,2,2,4]
Output: 8

Input: heights = [2,4]
Output: 4

Solution plan:
	
Monotonic Stack
Area=H×(Right Boundary−Left Boundary).

Pop each (index, value) then calculate current area.

For carry back, we can push (first index, smaller value), since the index and height is tracked.

After the first loop to build the stack with possible best rectangle points.

If an histogram is always increasing, it is possible for the stack to have multiple values after the main iteration is completed. Therefore, we can append a 0 to the initial array to ensure the end is always shorter.
"""

def largestRectangleInHistogram(heights: list):
	stk = []
	maxArea=0
	heights.append(0)
	for i, val in enumerate(heights):
		# start index for the possible rectangle
		start = i
		while stk and stk[-1][1]>val:
			j, height = stk.pop()
			maxArea = max(maxArea, height*(i - j))
			start = j #for carry back
			# The current shorter bar 'height' could have started at 'j'
		# build stack on the fly
		stk.append((start, val))
	return maxArea

print(largestRectangleInHistogram([7,1,7,2,2,4]))