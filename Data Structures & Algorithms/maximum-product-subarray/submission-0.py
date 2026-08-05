class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_end = min_end = result = nums[0]

        for i in range(1, len(nums)):

            curr = nums[i]

            if nums[i] < 0:
                min_end, max_end = max_end, min_end
            
            max_end = max(curr, curr * max_end)
            min_end = min(curr, curr * min_end)

            result = max(result, max_end)
        
        return result
