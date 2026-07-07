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
        res = []
        queue = deque([(root, 0)])
        while queue:
            node, lvl = queue.popleft()
            if lvl == len(res) - 1:
                if res:
                    res[-1] = node.val
                else:
                    res.append(node.val)
            else:
                res.append(node.val)
            
            if node.left:
                queue.append((node.left, lvl+1))
            if node.right:
                queue.append((node.right, lvl+1))
        return res