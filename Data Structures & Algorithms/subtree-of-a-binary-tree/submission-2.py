# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None or q is None:
            return p==q
        
        if p.val != q.val:
            return False
            
        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)

        return isLeftSame and isRightSame

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return root==subRoot
    
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
            

        isLeftSubtree = self.isSubtree(root.left, subRoot) 
        if isLeftSubtree:
            return True

        isRightSubtree =  self.isSubtree(root.right, subRoot)
        if isRightSubtree:
            return True
        
        return False