class Queue:
   def __init__(self):
      self.a1 = []
      self.a2 = []
   
   def enqueue(self, data):
      self.a1.append(data)
   
   def dequeue(self):
      if not self.a2:
         while self.a1:
            self.a2.append(self.a1.pop())
      if not self.a2: print("empty"); return None
      else:
         return self.a2.pop()

   def peek(self):
      if not self.a2:
         while self.a1:
            self.a2.append(self.a1.pop())
      if not self.a2: print("empty"); return None
      else:
         return self.a2[-1]
   
   def empty(self):
      return True if ((not self.a2) and (not self.a1)) else False

q1 = Queue()

q1.enqueue(1)
q1.enqueue(9)
q1.enqueue(8)
q1.enqueue(4)
print(q1.dequeue())
print(q1.peek())
print(q1.empty())