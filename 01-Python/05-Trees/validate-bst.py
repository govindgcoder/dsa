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

def validateBST(root):
   def validate(root, min, max):
      if root is None: return True

      if not min < root.val < max:
         return False
      
      return validate(root.left,min,root.val) and validate(root.right,root.val, max)
   return validate(root, float('-inf'), float('inf'))
      

root1 = TreeNode(5)
root1.left = TreeNode(2, TreeNode(1), TreeNode(3))
root1.right = TreeNode(7)

print(validateBST(root1))

root2 = TreeNode(8)
root2.left = TreeNode(5, TreeNode(4), TreeNode(7))
root2.right = TreeNode(2)

print(validateBST(root2))