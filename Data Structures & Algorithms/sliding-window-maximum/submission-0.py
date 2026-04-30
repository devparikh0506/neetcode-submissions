class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        
        left = 0
        right = k


        for right in range(k, len(nums)+1):
            left = right - k
            res.append(max(nums[left:right]))
        return res