# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum

            if node is None:
                return 0

            # Ignore a subtree if it reduces the path sum.
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Best complete path whose highest node is the current node.
            current_path_sum = node.val + left_gain + right_gain

            max_sum = max(max_sum, current_path_sum)

            # Parent can extend through only one branch.
            return node.val + max(left_gain, right_gain)
        max_gain(root)
        return max_sum
