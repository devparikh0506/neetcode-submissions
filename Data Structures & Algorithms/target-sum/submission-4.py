class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        total = sum(nums)

        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        S = (total + target) // 2

        dp = [0] * (S+1)
        dp[0] = 1

        for num in nums:
            for i in range(S, num-1, -1):
                dp[i] += dp[i-num]
        
        return dp[S]