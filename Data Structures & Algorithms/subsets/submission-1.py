class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(idx):

            res.append(curr.copy())

            for i in range(idx, len(nums)):
                curr.append(nums[i])

                backtrack(i+1)
            
                curr.pop()
        
        backtrack(0)
        return res