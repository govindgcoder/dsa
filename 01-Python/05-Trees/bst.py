class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def searchBST(root, val):

   if root is None or root.val == val:
      return root

   if val<root.val:
      return searchBST(root.left,val)
   else:
      return searchBST(root.right,val)

def insert(root, val):
   if root is None:
      return TreeNode(val=val)
   if val<root.val:
      root.left = insert(root.left,val)
   else: root.right = insert(root.right,val)
   return root

# Test cases
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)

    # Test case 1: Value found
    result1 = searchBST(root, 2)
    print(f"Searching for 2: {result1.val if result1 else 'Not Found'}") # Expected: 2

    # Test case 2: Value not found
    result2 = searchBST(root, 5)
    print(f"Searching for 5: {result2.val if result2 else 'Not Found'}") # Expected: Not Found
    
    # Test case for insertion
    result3 = searchBST(root, 11)
    print(f"Searching for 11: {result3.val if result3 else 'Not Found'}") # Expected: Not Found
    root=insert(root, 11)
    result3 = searchBST(root, 11)
    print(f"Searching for 11: {result3.val if result3 else 'Not Found'}") # Expected: 11