class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n!=m:
            return False
        
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        for c in t:
            if freq[ord(c) - ord('a')] <= 0:
                return False
            freq[ord(c) - ord('a')] -= 1
        return True
            
