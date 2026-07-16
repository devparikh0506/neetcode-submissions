class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(open_count, close_count):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            
            if open_count < n:
                curr.append('(')
                backtrack(open_count+1, close_count)
                curr.pop()
            
            if open_count > close_count:
                curr.append(")")
                backtrack(open_count, close_count+1)
                curr.pop() 
        backtrack(0, 0)
        return res
