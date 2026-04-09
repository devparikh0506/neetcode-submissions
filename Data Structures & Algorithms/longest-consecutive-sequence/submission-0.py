class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        result = 0

        for num in nums:
            if num-1 not in hashset:
                x = num
                counter  = 0

                while x in hashset:
                    counter +=1 
                    x+=1 
                result = max(counter, result)

        return result