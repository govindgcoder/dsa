# Repo to keep track of DSA problems I've been learning

---

### Basics with Python
Total: 29 🚀(?)

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
| 16 | Trees | [Diameter of Tree](./01-Python/05-Trees/dia-of-bst.py) | Recursive - similar to height - at each step, update max diameter | 🟢 |
|17 | HashMaps | [Valid Anagram](./01-Python/06-HashMaps/valid-anagram.py) | using hashmap, compare character frequency after length - T.C O(n) - S.C O(n) | 🟢 |
| 18 | HashMaps | [Two Sums](./01-Python/06-HashMaps/two-sums.py) | store num in hashmap(dict), find and retrieve complement if present - O(n^2) -> O(n) | 🟢 |
| 19 | HashMaps | [Group Anagrams](./01-Python/06-HashMaps/group-anagrams.py) | sorted tuple of chars as key, T.C O(n x k log k), S.C O(nk) <= n is no: of strings and k is the no: of chars | 🟡 |
| 20 | Sorting | [Merge sorted arrays](./01-Python/07-Sorting/merge-sorted-arrays.py) | merge two sorted arrays into one sorted array, used three pointers: nums1=[a,b,0,0], nums2=[c,d] | 🟢 |
| 21 | Sorting | [Merge Sort](./01-Python/07-Sorting/merge-sort.py) | divide and conquer, recursively split arrays, merge sorted halves, T.C O(nlogn), S.C O(n) | 🟡 |
| 22 | Sorting | [Quick Sort](./01-Python/07-Sorting/quick-sort.py) | divide and conquer, partitioning, recursive sorting, T.C avg:O(nlogn) worst:O(n2) , S.C O(logn)| 🟡 |
| 23 | Searching | [Search Insert Position](./01-Python/08-Binary-Search/search-insert-pos.py) | Binary search to find the target or the position where it would be inserted | 🟢 |
| 24 | Searching | [Search in Rotated Sorted Array](./01-Python/08-Binary-Search/search-rotated-sorted-arr.py) | Modified binary search, identify sorted half, adjust search range accordingly, O(logn) | 🟡 |
| 25 | Graphs | [Adjacency List, BFS, DFS](./01-Python/09-Graphs/adjacency-list.py) | adjacency list representation, BFS for level-order traversal, DFS for depth exploration | 🟡 |
| 26 | Graphs | [Number of Islands](./01-Python/09-Graphs/number-of-islands.py) | DFS to explore connected components, mark visited by sinking them (1->0), update count, T.C O(m*n)| 🟡 |
| 27 | Recursion | [All Subsets](./01-Python/10-Recursion/all-subsets.py) | Backtracking, explore - include & exclude each element| 🟡 |
| 28 | Recursion | [All Permutations](./01-Python/10-Recursion/all-permutations.py) | Backtracking, swap elements to generate permutations| 🟡 |
| 29 | Dynamic Programming | [Climbing Stairs](./01-Python/11-Dynamic-Programming/climbing-stairs.py) | Fibonacci sequence approach, T.C O(n), S.C O(1) | 🟢 |
---

---
> 01-Python (Priority): To learn DSA and build up Python Expertise at the same time, useful for System design and ML.
---
> 02-C: Some DSA Practise using C, building expertise in both of them. Have a transfarreble knowledge in it, for low-level and application programming. It was also part of my curriculum.
