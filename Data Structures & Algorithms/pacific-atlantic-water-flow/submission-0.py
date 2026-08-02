from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        n, m = len(heights), len(heights[0])

        def dfs(r, c, visited, prev_height):
            nonlocal m, n, heights
            if (
                (r, c) in visited
                or r < 0
                or r >= n
                or c < 0
                or c >= m
                or heights[r][c] < prev_height
            ):
                return

            visited.add((r,c))
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in dirs:
                dfs(r+dr, c+dc, visited, heights[r][c])
        pacific = set()
        atlantic= set()
       
        
        for c in range(m):
            dfs(0, c, pacific, heights[0][c])
        for r in range(n):
            dfs(r, 0, pacific, heights[r][0])
        
        for c in range(m):
            dfs(n - 1, c, atlantic, heights[n-1][c])
        for r in range(n):
            dfs(r, m - 1, atlantic, heights[r][m-1])
        
        return [list(tup) for tup in pacific & atlantic]
