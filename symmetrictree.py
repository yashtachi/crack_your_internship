class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def same( left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and same(left.left, right.right) and same(left.right, right.left)

        if not root:
            return True
        return same(root.left, root.right)