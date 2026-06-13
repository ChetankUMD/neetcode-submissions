class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        dic = defaultdict(int)
        maxf = 0
        l=0
        for r in range(n):
            dic[s[r]]+=1
            maxf = max(maxf, dic[s[r]])

            while (r-l+1) - maxf > k:
                dic[s[l]] -= 1
                l+=1
            res = max(r-l+1, res)
        
        return res
