"""
You are given an m x n integer matrix matrix with the following two properties:
	Each row is sorted in non-decreasing order.

	The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Solution approach:
	
think of matrix as a long array
	left=0
	right=m*n-1
	loop while left<=right:
		mid = left+ (right-left)  //2
		curr = mtx[mid//n][mid%n]
		if target==curr: return true
		else if target < curr:
			right=mid-1
		else:
			left=mid+1
	return false
"""

def search(mat: list[list[int]], target: int):
	m = len(mat)
	n = len(mat[0])
	left = 0
	right = m*n-1
	while(left<=right):
		mid = left + (right-left)//2
		curr = mat[mid//n][mid%n]
		if curr==target:
			return True
		elif target < curr:
			right = mid-1
		else:
			left = mid+1
	return False
	
print(search([[1,2,5],[8,11,13]], 12))