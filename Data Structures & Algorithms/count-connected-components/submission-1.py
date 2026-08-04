class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(x, y):
            x_root, y_root = find(x), find(y)

            if x_root != y_root:
                parent[y_root] = x_root
        
        for x, y in edges:
            union(x, y)
        
        return len({ find(i) for i in range(n)})
        