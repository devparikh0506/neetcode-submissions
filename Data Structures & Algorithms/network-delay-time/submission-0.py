from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        pq = [(0, k)]

        while pq:
            d, node = heapq.heappop(pq)

            if node in dist:
                continue
            dist[node] = d

            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (d + weight, neighbor))

        if len(dist) != n:
            return -1

        return max(dist.values())