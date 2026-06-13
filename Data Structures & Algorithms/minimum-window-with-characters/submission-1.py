class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h1 = {}
        h2 = {}
        minc = float("inf")
        resl = 0
        resr = 0
        for c in t:
            h1[c] = 1+ h1.get(c, 0)
        l = 0
        have,  need = 0, len(h1)
        for r in range(len(s)):
            h2[s[r]] = 1+h2.get(s[r], 0)

            if s[r] in h1 and h2[s[r]] == h1[s[r]]:
                have+=1
            
            while have == need:
                if (r-l+1) < minc:
                    resl = l
                    resr = r
                    minc = r-l+1
                
                h2[s[l]]-=1
                if s[l] in h1 and h2[s[l]] < h1[s[l]]:
                    have -=1
                l+=1
        
        return s[resl : resr +1] if minc != float("inf") else ""
            
            

                    