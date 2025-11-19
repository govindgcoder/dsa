class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


def insert(root, val):
   if root is None:
      return TreeNode(val=val)
   if val<root.val:
      root.left = insert(root.left,val)
   else: root.right = insert(root.right,val)
   return root

def inorder(root):
   if root is None: return root
   print('(',end='')
   inorder(root.left)
   print(root.val, end='')
   inorder(root.right)
   print(')',end='')


root = TreeNode(5)
insert(root, 3)
insert(root, 8)
insert(root, 6)
insert(root, 1)
insert(root, 4)

inorder(root)