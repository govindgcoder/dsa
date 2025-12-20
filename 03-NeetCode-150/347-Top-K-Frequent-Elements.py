"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""

nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
# naive solution
# def topKfrequent(nums,k):
#     map = {}
#     for i in nums:
#         if i not in map:
#             map[i]=0
#         map[i]+=1
#     ordered = sorted(map.items(),key=lambda item: item[1],reverse=True)
#     print(ordered)
#     keys = list(_[0] for _ in ordered)
#     return keys[:k]


def topKfrequent(nums, k):
    count = {}
    n = len(nums)
    m = k
    freq = [[] for _ in range(n + 1)]
    res = []
    for i in nums:
        count[i] = 1 + count.get(i, 0)
    for i, j in count.items():
        freq[j].append(i)
    for i in range(n - 1, 0, -1):
        for j in freq[i]:
            res.append(j)
            m -= 1
            if m == 0:
                return res


print(topKfrequent(nums, k))
