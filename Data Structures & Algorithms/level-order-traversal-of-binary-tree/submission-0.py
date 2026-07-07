# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue  = deque([(root, -1)])
        curr = 0
        while queue:

            node, lvl  = queue.popleft()
            if lvl != curr:
                curr=lvl
                result.append([node.val])
            else:
                result[-1].append(node.val)
            
            if node.left:
                queue.append((node.left, curr+1))

            if node.right:
                queue.append((node.right, curr+1))
        return result