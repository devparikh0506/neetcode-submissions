class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def getRoot(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootx, rooty = getRoot(x), getRoot(y)
            if rootx == rooty:
                return False
            parent[rootx] = rooty
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True