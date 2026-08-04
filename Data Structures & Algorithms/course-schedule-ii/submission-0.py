from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses

        adj = [[] for _ in range(numCourses)]

        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v] +=1
        
        q = deque([ c for c in range(numCourses) if indegree[c]==0])
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for v in adj[c]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
            
        
        return order if len(order)==numCourses else []


