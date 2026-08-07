class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n<= 1:
            return 0

        hold = float("-inf")
        sold = 0
        rest = 0

        for price in prices:
            ph, ps, pr = hold, sold, rest
            hold = max(ph, pr-price)
            sold = ph + price
            rest = max(pr, ps)
        return max(sold, rest)
