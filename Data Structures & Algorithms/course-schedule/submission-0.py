class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def isCyclic(adj, u, visited, processing):

            if processing[u]:
                return True
            if visited[u]:
                return False
            
            visited[u]=True
            processing[u]=True

            for v in adj[u]:
                if isCyclic(adj, v, visited, processing):
                    return True
            
            processing[u]=False
            return False
        
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
        
        visited = [False] * numCourses
        processing = [False] * numCourses
        for i in range(numCourses):
            if isCyclic(adj, i, visited, processing ):
                return False
        return True