class MinStack:
   def __init__(self):
      self.arr = []
      self.mins = []
   
   def min(self,a):
      if not self.mins or a<=self.mins[-1]:
         self.mins.append(a)

   def push(self,val):
      self.arr.append(val)
      self.min(val)
   
   def pop(self):
      val = self.arr.pop()
      if val == self.mins[-1]:
         self.mins.pop()
      return val

# Boilerplate for testing
if __name__ == "__main__":
   minStack = MinStack()
   # Test cases can be added here
   minStack.push(5)
   minStack.push(2)
   minStack.push(8)
   minStack.push(1)
   print(f"Popped: {minStack.pop()}") # Should pop 1
   print(f"Current min: {minStack.mins[-1]}") # Should be 2
   print(f"Popped: {minStack.pop()}") # Should pop 8
   print(f"Current min: {minStack.mins[-1]}") # Should be 2