"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

def binary_search(num, target):
	left = 0
	right = len(num)-1
	while left<=right:
		mid = left + (right-left)//2
		if num[mid]==target:
			return mid
		elif num[mid]<target:
			left = mid+1
		else:
			right = mid-1
	return -1
		

print(binary_search([1,2,3,5,6], 2))