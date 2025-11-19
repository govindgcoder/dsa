arr = [4, 5, 2, 10, 8]

def nextGreaterArr(arr):
   stk = []
   n=len(arr)
   result = [-1]*n

   for i in range(n):
      curr = arr[i]
      while stk and curr > arr[stk[-1]]:
         prev = stk.pop()
         result[prev] = curr
      stk.append(i)

   return result

print(arr)
print(nextGreaterArr(arr))