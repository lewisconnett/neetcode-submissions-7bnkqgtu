# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []

        order = []

        return self.inorderTraversal(root, order, k)

    def inorderTraversal(self, root: Optional[TreeNode], order: List[int], k) -> int:
        if not root:
            return None

        left = self.inorderTraversal(root.left, order, k)

        if left is not None:
            return left

        order.append(root.val)

        if len(order) == k:
            return root.val

        return self.inorderTraversal(root.right, order, k)
