class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(index, curr):
            if index == n:
                return 1 if curr == target else 0
            if (index, curr) in memo:
                return memo[(index, curr)]
            result = dfs(index+1, curr + nums[index]) + dfs(index+1, curr - nums[index])
            memo[(index, curr)] = result
            return result
        return dfs(0, 0)