class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for t in range(n):
            while stack and temperatures[stack[-1]] < temperatures[t]:
                i = stack.pop()
                res[i] = t - i
            stack.append(t)
        return res
