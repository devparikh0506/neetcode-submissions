class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                res = max(res, height * width)
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left- 1
            res = max(res, height * width)
        
        return res