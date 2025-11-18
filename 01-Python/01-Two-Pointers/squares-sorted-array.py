nums = [-4, -1, 0, 3, 10]

def squares(arr):
   l = 0
   r = len(arr)-1
   result = list(0 for i in range(len(arr)))
   for k in range((len(arr)-1), -1 ,-1): #the end is not included remember
      if arr[l]**2 > arr[r]**2:
         result[k] = arr[l]**2
         l+=1
      else:
         result[k] = arr[r]**2
         r-=1
   return result
print(nums)
print(squares(nums))