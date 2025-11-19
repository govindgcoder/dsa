class Node:
   def __init__(self,data,next=None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = None

   def insertAtBegin(self,data):
      newNode = Node(data)
      newNode.next = self.head
      self.head = newNode

   def display(self):
      temp = self.head
      while temp is not None:
         print(temp.data,end='->')
         temp=temp.next
      print("None")
   
   def removeNthFromEnd(self,n):
      dummy=Node(0,self.head)
      s = f = dummy
      dist = 0
      while(f.next is not None and dist<n):
         f=f.next
         dist+=1
      while(f.next is not None):
         s=s.next
         f=f.next
      s.next=s.next.next
      self.head = dummy.next
      

ll = LinkedList()
ll.insertAtBegin(9)

ll.display()
ll.removeNthFromEnd(2)
ll.display()