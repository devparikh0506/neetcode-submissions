from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or not s:
            return ''
        
        t_counts = defaultdict(int)
        
        for c in t:
            t_counts[c]+=1
        
        required = len(t_counts)

        w_counts = defaultdict(int)
        formed = 0

        ans = float("inf"), None, None
        left = 0
        for right in range(len(s)):
            char = s[right]

            w_counts[char]+=1

            if char in t_counts and t_counts[char]==w_counts[char]:
                formed+=1
            
            while left <= right and formed==required:
                char = s[left]
                
                if (right-left +1) < ans[0]:
                    ans = (right-left +1), left, right

                w_counts[char]-=1

                if char in t_counts and w_counts[char] < t_counts[char]:
                    formed-=1
                
                left+=1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
