from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((t, v))
        
        visited = [False] * (n+1)
        distances = [float('inf')] * (n+1)

        pq = [(0, k)]

        while pq:

            time, node = heapq.heappop(pq)

            if visited[node]:
                continue
            
            visited[node] = True
            distances[node] = time

            for td, neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                if distances[neighbor] > time + td:
                    distances[neighbor] = time + td
                    heapq.heappush(pq, (time + td, neighbor))

        return max(distances[1:]) if max(distances[1:]) < float('inf') else -1
