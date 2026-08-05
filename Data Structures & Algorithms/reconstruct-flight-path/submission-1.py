from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for u,v in tickets:
            heapq.heappush(graph[u], v)   
        
        path = []

        def visit(node):
            while graph[node]:
                next_node = heapq.heappop(graph[node])
                visit(next_node)
            path.append(node)
        
        visit("JFK")
        return path[::-1]