from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_f = 0
        res = 0
        counts = defaultdict(int)
        for right in range(len(s)):
            counts[s[right]] += 1

            max_f = max(max_f, counts[s[right]])

            while ((right - left + 1) - max_f) > k:
                counts[s[left]]-=1
                left+=1
            
            res = max(res, (right - left + 1))
        return res


