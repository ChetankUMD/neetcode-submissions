class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        i = j = res = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                j += 1
            i += 1
            
        return res




        # res = 0
        # g.sort(reverse=True)
        # s.sort(reverse=True)
        # for i in range(len(g)):
        #     for j in range(len(s)):
        #         if s[j]>=g[i]:
        #             res+=1
        #             s.pop(j)
        #             break

        # return res