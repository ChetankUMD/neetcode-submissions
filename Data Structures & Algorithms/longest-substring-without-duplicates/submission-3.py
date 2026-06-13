class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        h = [s[0]] 
        l,r = 0,1
        res = 1

        while r<len(s):
            while s[r] in h:
                h.remove(s[l])
                l+=1
            res = max(res, (r-l+1))
            h.append(s[r])
            r+=1
        
        return res