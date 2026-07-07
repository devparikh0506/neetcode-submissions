# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, pathMax):
            if not node:
                return
            nonlocal res
            if node.val >= pathMax:
                res+=1
            dfs(node.left, max(pathMax, node.val))
            dfs(node.right, max(pathMax, node.val))
        dfs(root, root.val)
        return res

