class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def maxDepth(root):
   if root is None: return 0
   left = maxDepth(root.left)
   right = maxDepth(root.right)
   return 1 + (left if left>right else right)

# Test cases
# Test case 1: Empty tree
root1 = None
print(f"Max depth of an empty tree: {maxDepth(root1)}") # Expected: 0

# Test case 2: Single node tree
root2 = TreeNode(1)
print(f"Max depth of a single node tree: {maxDepth(root2)}") # Expected: 1

# Test case 3: Simple tree
root3 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(f"Max depth of tree [3,9,20,null,null,15,7]: {maxDepth(root3)}") # Expected: 3

# Test case 4: Skewed tree (left)
root4 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
print(f"Max depth of skewed left tree: {maxDepth(root4)}") # Expected: 4

# Test case 5: Skewed tree (right)
root5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
print(f"Max depth of skewed right tree: {maxDepth(root5)}") # Expected: 4

# Test case 6: Balanced tree
root6 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(f"Max depth of balanced tree: {maxDepth(root6)}") # Expected: 3
