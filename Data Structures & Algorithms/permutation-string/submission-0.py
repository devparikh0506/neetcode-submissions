from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n1])

        if window_counts == s1_counts:
            return True

        for right in range(n1 , n2):
            left = right - n1
            window_counts[s2[left]]-=1
            window_counts[s2[right]]+=1

            if window_counts[s2[left]] == 0:
                del window_counts[s2[left]]

            if window_counts == s1_counts:
                return True
        return False