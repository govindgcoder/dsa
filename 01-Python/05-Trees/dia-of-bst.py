class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_max_dia(self, root):
        self.max_dia = 0

        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)

            curr = left + right
            print(curr)
            self.max_dia = max(curr, self.max_dia)

            return 1 + max(left, right)

        height(root)
        return self.max_dia


root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(
        2,
        TreeNode(2),
        TreeNode(2),
    ),
)
s1 = Solution()
print(s1.get_max_dia(root))
