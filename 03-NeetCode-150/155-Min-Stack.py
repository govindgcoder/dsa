"""
Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1)O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

Constraints:
    -2^31 <= val <= 2^31 - 1.
    pop, top and getMin will always be called on non-empty stacks.

Solution:

a python list can easily act as a stack. another stack is built by pushing the minimum of last minimum or current val.
<- the minimum stack
"""
class MinStack:
    def __init__(self):
        self.arr = []
        self.minS = []
    def push(self, val):
        self.arr.append(val)
        if self.minS and self.minS[-1]<val:
            self.minS.append(self.minS[-1])
        else:
            self.minS.append(val)
    def pop(self):
        self.arr.pop()
        self.minS.pop()
    def top(self):
        return self.arr[-1]
    def getMin(self):
        return self.minS[-1]

minStack = MinStack() 
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin()
minStack.pop()
minStack.top()    # return 2
minStack.getMin() # return 1

print(minStack.arr)