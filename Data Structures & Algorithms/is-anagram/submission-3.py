class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        for c in s:
            h1[c] = h1.get(c,0)+1
        
        h2 = {}
        for c in t:
            h2[c] = h2.get(c,0)+1
        print(h1)
        print(h2)
        return h1==h2