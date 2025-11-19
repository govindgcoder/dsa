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
   
   def reverse(self):
      if(self.head is None):
         print("Empty linked list")
         return
      prev = None
      curr = self.head
      nex = curr.next
      while(curr is not None):
         nex = curr.next
         curr.next = prev
         prev = curr
         curr=nex
      self.head=prev

ll = LinkedList()
ll.insertAtBegin(9)
ll.insertAtBegin(2)
ll.insertAtBegin(3)
ll.insertAtBegin(7)
ll.insertAtBegin(5)
ll.display()
ll.reverse()
ll.display()
