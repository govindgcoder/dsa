def running_sum(nums):
   for i in range(len(nums)-1):
      nums[i+1] = nums[i+1]+nums[i]

nums = [1, 2, 3, 4]
running_sum(nums)
print(nums) # Should output [1, 3, 6, 10]