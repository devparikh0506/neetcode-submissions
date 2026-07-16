class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def backtrack(idx, remaining):

            if remaining == 0:
                res.append(curr.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])

                backtrack(i, remaining - nums[i])

                curr.pop()
            
        backtrack(0, target)
        return res
