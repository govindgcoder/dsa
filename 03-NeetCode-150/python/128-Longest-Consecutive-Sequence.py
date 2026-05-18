"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
import heapq

nums= [1,0,1,2]

# nlogn
# def longestCS(nums):
#     heapq.heapify(nums)
#     maxc=0
#     sum=1
#     prev=None
#     for i in range(len(nums)):
#         curr = heapq.heappop(nums)
#         if curr==prev:
#             continue
#         if prev is None or curr-1!=prev:
#             print("nyaa")
#             sum=1
#         else:
#             sum+=1
#         prev=curr
#         maxc=sum if sum> maxc else maxc
#     print(maxc)

def longestCS(nums):
    numset = set(nums)
    n=0
    maxc=0
    for i in numset:
        curr = i
        if curr-1 not in numset:
            #start of a seq
            n=0
            while curr in numset:
                curr+=1
                n+=1
            maxc=max(maxc,n)
    return maxc

print(longestCS(nums))