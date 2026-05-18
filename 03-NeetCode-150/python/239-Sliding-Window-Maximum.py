"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

---

Solution plan:

build a max heap across window - only pop elements when the max element is outside the window uptill the current max is in the window.
store each max in the res array.
 	
"""

import heapq

def slidingWindowMaximum(nums,k):
	heap = []
	res = []
	# main loop for the sliding window
	for i in range(len(nums)):
		# build the heap as the window is moving
		heapq.heappush(heap, [-nums[i],i])
		
		# remove heap max which are not in the window
		# this will ensure minimal resources yet all values will be inevitably removed
		while heap[0][1]<=i-k:
			heapq.heappop(heap)
		
		# once the window is of the required size
		# get the current max and add it to the result
		if i>=k-1:
			res.append(-heap[0][0])
	return res

print(slidingWindowMaximum([1,3,-1,-3,5,3,6,7],3))

# for later note: check the ideal 'google' solution - O(N)