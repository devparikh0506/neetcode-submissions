class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        used  = [False] * len(nums)

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                
                if used[i]:
                    continue

                curr.append(nums[i])
                used[i] = True

                backtrack()

                curr.pop()
                used[i] = False
        
        backtrack()
        return res