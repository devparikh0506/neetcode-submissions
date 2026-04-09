class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {')':'(', "}" : "{", "]":"["}
        for c in s:
            if c in p_map:
                if not stack or stack[-1] != p_map[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack 
