"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""

nums = [4,1,-1,2,-1,2,3]
k = 2
#naive solution
def topKfrequent(nums,k):
    map = {}
    for i in nums:
        if i not in map:
            map[i]=0
        map[i]+=1
    ordered = sorted(map.items(),key=lambda item: item[1],reverse=True)
    print(ordered)
    keys = list(_[0] for _ in ordered)
    return keys[:k]
    
print(topKfrequent(nums,k))