class Solution:
    def countSubstrings(self, s: str) -> int:
        
        t = "#" + "#".join(s) + "#"

        n = len(t)

        p = [0] * n
        c = 0

        r = 0

        for i in range(1, n-1):

            mirror = (2 * c) - i

            if i < r:
                p[i] = min(r-i, p[mirror])
            

            while 0<= (i - p[i] - 1) and n >  (i + p[i] + 1) and t[i - p[i] - 1]==t[ i + p[i] + 1]:
                p[i] += 1
            
            if i + p[i] > r:
                r = i+p[i]
                c = i
        

        return sum([(val+1)//2 for val in p])