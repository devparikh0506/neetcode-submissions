class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:

        n = len(s)
        i = 0

        decoded = []
        while i < n:

            j = i
            while s[j] !='#':
                j+=1
            
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            i = j+1+length
            decoded.append(word)
        return decoded