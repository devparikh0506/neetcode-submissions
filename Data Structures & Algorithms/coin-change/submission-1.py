from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque()
        q.append((0, amount))
        visited = {amount}
        while q:
            used, remaining = q.popleft()

            if remaining == 0:
                return used
            
            for coin in coins:
                if (remaining - coin) >= 0 and (remaining - coin) not in visited:
                    visited.add(remaining - coin)
                    q.append((used+1, remaining - coin))
        
        return -1