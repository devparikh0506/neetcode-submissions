from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((t, v))
        
        visited = [False] * (n+1)
        times = [float('inf')] * (n+1)

        pq = [(0, k)]

        while pq:

            time, node = heapq.heappop(pq)

            if visited[node]:
                continue
            
            visited[node] = True
            times[node] = time

            for td, neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                if times[neighbor] > time + td:
                    times[neighbor] = time + td
                    heapq.heappush(pq, (time + td, neighbor))

        return max(times[1:]) if max(times[1:]) < float('inf') else -1
