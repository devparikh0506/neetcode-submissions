class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ""

        start, max_len = 0, 1

        def expand(left, right):

            while left >=0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            
            return right - left - 1
        
        for i in range(len(s)):
            prev1 = expand(i,i)
            prev2 = expand(i,i+1)

            current = max(prev1, prev2)

            if current > max_len:
                max_len = current
                start = i - (current-1) // 2
            
        return s[start:start+max_len]

                 