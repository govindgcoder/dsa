class Node:
   def __init__(self,key, data: int, next=None):
      self.key=key
      self.data=data
      self.next=None
   def add(self, key, data):
      temp = self
      while temp.next is not  None:
         temp=temp.next
      temp.next=Node(key,data)
   def print_node(self,key):
      current=self
      while current!=None:
         if current.key==key:
            print(f"{current.key}: {current.data}", end="  ")
            return
         current=current.next
      print("not found")
      print()

def _hash_key(key):
      return len(key)%10

class Hash:
   def __init__(self, size=10):
      self.table = [None] * size

   def put(self,key, data):
      hashcode=_hash_key(key)
      if not self.table[hashcode]:
         self.table[hashcode]=Node(key, data)
      else:
         self.table[hashcode].add(key, data)
   def get(self, key):
      hashcode=_hash_key(key)
      if not self.table[hashcode]:
         print("empty")
      else:
         self.table[hashcode].print_node(key)

test = Hash()
test.put("govind",112)
test.put("roshan", 222)
test.get("roshan")



   
