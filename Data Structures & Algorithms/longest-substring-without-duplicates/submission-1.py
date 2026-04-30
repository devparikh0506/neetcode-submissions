from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        right = 0
        max_len = 0
        counts = defaultdict(int) 
        while right < len(s):
            counts[s[right]] += 1
            while counts[s[right]] > 1:
                counts[s[left]] -= 1
                left += 1 
            max_len = max(max_len, right-left+1)
            right+=1
        return max_len