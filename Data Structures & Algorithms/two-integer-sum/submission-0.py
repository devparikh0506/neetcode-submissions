class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = dict()

        for i in range(len(nums)):

            if mapping.get(nums[i]) is not None:
                return [mapping.get(nums[i]), i]
            
            mapping[target - nums[i]] = i
        return []
