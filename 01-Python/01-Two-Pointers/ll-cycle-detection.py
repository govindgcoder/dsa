class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print()

    def has_cycle(self):
        if self.head is None:
            print("Empty linked list")
            return False
        s = f = self.head
        while f.next is not None and f.next.next is not None:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False

    def make_cycle(self, position):
        if self.head is None:
            return

        tail = self.head
        while tail.next:
            tail = tail.next

        if position == -1:  # No cycle
            return

        cycle_node = self.head
        for _ in range(position):
            if cycle_node is None:  # Position out of bounds
                return
            cycle_node = cycle_node.next

        tail.next = cycle_node


ll = LinkedList()
ll.insertAtBegin(5)
ll.insertAtBegin(4)
ll.insertAtBegin(3)
ll.insertAtBegin(2)
ll.insertAtBegin(1)
ll.display()
print(ll.has_cycle())
ll.make_cycle(
    2
)  # Creates a cycle where the tail points to the node at index 2 (0-indexed)
print(ll.has_cycle())

ll2 = LinkedList()
ll2.insertAtBegin(3)
ll2.insertAtBegin(2)
ll2.insertAtBegin(1)
ll2.display()
print(ll2.has_cycle())
ll2.make_cycle(-1)  # No cycle
print(ll2.has_cycle())
