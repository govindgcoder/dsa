arr = [1,3,0,9,6,0,3]
#So, we gotta move the zeroes to the end while maintaining the relative order of the other elements.

#define two pointers
# def moveZeroes(arr):
#    read = 0
#    write = 0
#    while (read < len(arr)):
#       if (arr[read] != 0):
#          arr[write] = arr[read]
#          print(read,' ',write)
#          write += 1
#       read += 1
#    while(write < len(arr)):
#       arr[write]=0
#       write+=1

#    return arr

def moveZeroes(arr):
   write=0
   for read in range(len(arr)):
      if arr[read]!=0:
         arr[write],arr[read]=arr[read],arr[write]
         write+=1

   return arr

print(arr)
arr = moveZeroes(arr)
print(arr)