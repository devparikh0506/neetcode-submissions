from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num]+= 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []
        count = 0
        for i in range(len(buckets)-1, 0, -1):

            for num in buckets[i]:
                result.append(num)
                count+=1
                if count==k:
                    return result
