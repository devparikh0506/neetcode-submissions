class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        
        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(prev2+nums[i], prev1)
            prev2, prev1 = prev1, curr
        
        return max(prev2, prev1)