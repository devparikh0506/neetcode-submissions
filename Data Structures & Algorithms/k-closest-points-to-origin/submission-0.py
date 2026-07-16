import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for point in points:
            distances.append((math.sqrt(point[0]**2 + point[1]**2), point[0], point[1]))

        heapq.heapify(distances)

        res = []
        for i in range(k):
            _, x, y = heapq.heappop(distances)
            res.append([x, y])
        return  res