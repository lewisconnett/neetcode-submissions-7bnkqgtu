# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])

        while len(queue) > 0:
            level = []
            for i in range(0, len(queue)):
                front = queue.popleft()
                level.append(front.val)

                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)

            ans.append(level)

        return ans
