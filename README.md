# Repo to keep track of DSA problems

---

### Python
Total: 15 🚀(?)

---

| Index | Category | Problem | Note | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Two Pointers | [Move zeroes](./01-Python/01-Two-Pointers/move-zeroes.py) | read and write pointers, incorporate swap for optimization | 🟢 |
| 2 | Two Pointers | [Squares sorted array](./01-Python/01-Two-Pointers/squares-sorted-array.py) | left and right to squares for max, k to track the posn of max in result - k is decreasing | 🟢 |
| 3 | Arrays | [Running sum](./01-Python/02-Arrays/running-sum.py) | (Prefix sums start with 0, and have n+1 length) | 🟢 |
| 4 | Linked Lists | [Reverse given ll](./01-Python/03-Linked-lists/reverse-ll.py) | 3 pointers, return prev as head | 🟢 |
| 5 | Two Pointers | [Cycle Detection in linked lists](./01-Python/01-Two-Pointers/ll-cycle-detection.py) | Floyd cycle finding approach | 🟢 |
| 6 | Two Pointers | [Middle of Linked list](./01-Python/01-Two-Pointers/middle-of-ll.py) | return s if f.next is None else s.next | 🟢 |
| 7 | Two Pointers | [Remove Nth node from end of list](./01-Python/01-Two-Pointers/remove-nth-from-end.py) | two loops, make a window | 🟡 |
| 8 | Stacks | [Valid Paranthesis](./01-Python/04-Stacks/valid-para.py) | stack to keep track - brackets, mapping for brackets | 🟢 |
| 9 | Stacks | [Queue with stacks](./01-Python/04-Stacks/queue-with-stacks.py) | s1 to enq, deq = pouring all items from s1 to s2, then popping 2 | 🟢 |
| 10 | Stacks | [Minimum stack](./01-Python/04-Stacks/min-stack.py) | keep track of minimum values with another list, remember to also add equal values to it | 🟡 |
| 11 | Stacks | [Next greater array](./01-Python/04-Stacks/next-greater.py) | Monotonic stack, loop to iterate, loop for current\>stack elements: to pop stack, which tracks the indexes to be filled | 🟢 |
| 12 | Trees | [Max depth](./01-Python/05-Trees/max-depth.py) | Recursion - base case: 0 if leaf node, recursive: 1 + max(max depth of left, max depth of right) | 🟢 |
| 13 | Trees | [Validate BST](./01-Python/05-Trees/bst.py) | helper function with range, (initially from -inf to inf), left nodes < root val < right | 🟡 |
| 14 | Trees | [Recursive Tree traversal](./01-Python/05-Trees/recursive-tree-traversal.py) | recursion on left, right and then print root | 🟢 |
| 15 | Trees | [Iterative Tree traversal](./01-Python/05-Trees/iterative-tree-traversal.py) | recursion stack - explore till none on left - backtrack - check right at every step | 🟡 |
---
---
> 01-Python (Priority): To learn DSA and build up Python Expertise at the same time, useful for System design and ML.
---
> 02-C: Some DSA Practise using C, building expertise in both of them. Have a transfarreble knowledge in it, for low-level and application programming. It was also part of my curriculum.
