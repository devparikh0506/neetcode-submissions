from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid or not grid[0]:
            return None

        n = len(grid)
        m = len(grid[0])

        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    queue.append((i, j))
        
        dirs = [(0,1), (0,-1), (-1,0), (1, 0)]
        INF = 2**31 - 1
        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx = x+dx
                ny = y+dy

                if 0<= nx < n and 0<= ny < m and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))
