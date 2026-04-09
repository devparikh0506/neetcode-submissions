import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = 1
        maxRate = max(piles)

        while minRate <= maxRate:
            midRate =  (minRate + maxRate) // 2


            neededHours = 0 
            for p in piles:
                neededHours += math.ceil(p/midRate) 
            if neededHours <= h:
                maxRate = midRate - 1
            else:
                minRate = midRate + 1
            
        return minRate