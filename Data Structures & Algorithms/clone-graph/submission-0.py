"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def dfs(node):
            if not node:
                return None
            nonlocal oldToNew
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for nn in node.neighbors:
                copy.neighbors.append(dfs(nn))
            

            return copy

        return dfs(node)

