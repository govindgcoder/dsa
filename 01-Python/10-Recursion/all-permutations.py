nums = [1,2,3]

def permutations(nums):
    result=[]
    n=len(nums)
    def update(curr):
        print(result)
        if len(curr)==n:
            result.append(curr[:])
        for i in range(0, n):
            if nums[i] in curr:
                continue
            curr.append(nums[i])
            update(curr)
            curr.pop()
    update([])
    return result
    
print(permutations(nums))