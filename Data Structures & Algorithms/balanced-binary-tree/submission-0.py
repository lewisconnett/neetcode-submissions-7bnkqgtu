# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_subtree = self.height(root.left)
        right_subtree = self.height(root.right)

        difference = abs(left_subtree - right_subtree)

        if difference > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.height(root.left) + 1, self.height(root.right) + 1)