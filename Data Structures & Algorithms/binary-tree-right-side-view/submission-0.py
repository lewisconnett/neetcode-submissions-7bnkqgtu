# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        ans = []

        while len(queue) > 0:
            right_node = len(queue)
            for i in range(len(queue)):
                front = queue.popleft()
                if i == (right_node - 1):
                    ans.append(front.val)

                if front.left:
                    queue.append(front.left)

                if front.right:
                    queue.append(front.right)
                
                
        
        return ans

        
        