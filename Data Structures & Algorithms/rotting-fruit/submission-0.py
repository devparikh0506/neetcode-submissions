from collections import deque
class Solution:
    def isSafe(self,x, y, m ,n):
        return 0<=x<m and 0<=y<n
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        queue = deque()
        fresh = 0
        m , n = len(grid), len(grid[0])
        minutes = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i, j, 0))
        
        if fresh==0:
            return 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            x, y, elapsed = queue.popleft()
            
            minutes = max(elapsed, minutes)

            for dr, dc in dirs:
                nx, ny = x+dr, y+dc

                if self.isSafe(nx, ny, m ,n) and grid[nx][ny]==1:
                    grid[nx][ny]=2
                    fresh-=1
                    queue.append((nx, ny, elapsed+1))
        return minutes if fresh==0 else -1

