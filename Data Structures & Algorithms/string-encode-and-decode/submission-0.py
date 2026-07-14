class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        
        return res
    def decode(self, s: str) -> List[str]:
        dec = []
        i=0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            dec.append(word)
            i = j + 1 + length
        return dec