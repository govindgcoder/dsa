class Node:
   def __init__(self,data):
      self.data = data
      self.next = None

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
      print()
   
   def middle(self):
      if(self.head is None): return None
      s = self.head
      f = self.head
      while(f.next is not None and f.next.next is not None):
         s=s.next
         f=f.next.next
      return s if f.next is None else s.next

ll = LinkedList()
ll.insertAtBegin(9)
ll.insertAtBegin(2)
ll.insertAtBegin(3)
ll.insertAtBegin(7)
ll.insertAtBegin(5)
ll.display()
print(ll.middle().data)

ll2 = LinkedList()
ll2.insertAtBegin(2)
ll2.insertAtBegin(13)
ll2.insertAtBegin(8)
ll2.insertAtBegin(0)
ll2.display()
print(ll2.middle().data)