"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are:
	(i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

for two lines:
	area = smaller line * distance between them
for every line, the next one can either be smaller or higher
the best chance for maximizing area, is to move from the smaller line of the two while retaining the larger one.
to maximize distance between, lets use two pointer technique, left and right
^
|
Greedy approach

"""



def maxArea(height):
	lp = 0
	rp = len(height)-1
	maxVal = 0
	while(lp<rp):
		minVal = min(height[lp],height[rp])
		area = minVal*(rp-lp)
		maxVal = max(area, maxVal)
		if height[lp]==minVal:
			lp+=1
		else:
			rp-=1
	return maxVal

height = [1,1]
print(maxArea(height))