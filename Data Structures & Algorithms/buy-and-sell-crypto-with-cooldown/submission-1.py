class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ownStock = [0] * (len(prices))
        noStock = [0] * (len(prices))

        if len(prices) < 2:
            return 0

        ownStock[0] = -prices[0]
        ownStock[1] = max(-prices[0], -prices[1])
        noStock[1] = max(noStock[0], ownStock[0] + prices[1])

        for i in range(2, len(prices)):
            ownStock[i] = max(ownStock[i - 1], noStock[i - 2] - prices[i])
            noStock[i] = max(ownStock[i - 1] + prices[i], noStock[i - 1])


        return noStock[-1]
