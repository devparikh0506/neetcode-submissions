class Solution:
    def eval(self, n1, n2, op):
        if op=="+":
            return n1+n2
        elif op=="-":
            return n1-n2
        elif op=="*":
            return n1*n2
        else:
            return int(n1/n2)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ['+', '-', '*', '/']:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(self.eval(n1, n2, t))
            else:
                stack.append(int(t))
                
        return stack.pop()