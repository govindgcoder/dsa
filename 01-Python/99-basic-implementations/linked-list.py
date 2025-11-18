class Node:
   def __init__(self, data: int, next=None):
      self.data=data
      self.next=next


def add(head: Node, data):
   if head==None:
      head=Node(data, None)
      return head
   temp=head
   while temp.next!=None:
      temp=temp.next
   temp.next=Node(data,None)
   return head

def dell(head: Node, data):
   if head is None:
      print("empty\n")
      return
   if head.data==data:
      return head.next
   current = head
   while current.next is not None:
      if current.next.data==data:
         current.next=current.next.next
         return head
      current=current.next
   print("not found")

def display(head: Node):
   if head==None:
      print("empty")
      print()
   current=head
   while current!=None:
      print(f"{current.data}", end="  ")
      current=current.next
   print()

def main():
      head=None
      choice: int
      data: int
      while True:
         print("Linked list program");
         print("Choose your option: 1. add 2. delete 3. display 0. exit");
         choice=int(input("enter your choice: "))
         match choice:
            case 1:
               data = int(input("Enter your data: "))
               head = add(head, data)
            case 2:
               data = int(input("Enter your data to be deleted: "))
               head = dell(head, data)
            case 3:
               display(head)
            case 0:
               return

main()