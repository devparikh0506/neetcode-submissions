from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        current = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        def backtrack(start):
            
            if start == len(s):
                res.append(current.copy())
                return

            
            for end in range(start, len(s)):
                if not is_palindrome(start, end):
                    continue

                current.append(s[start:end + 1])

                backtrack(end + 1)

                current.pop()

        backtrack(0)
        return res