class Solution:
    def maxProfit(self, p: List[int]) -> int:
        n = len(p)

        def dfs(ind, buy):
            if ind>=n:
                return 0
            
            if buy:
                profit = max(-p[ind]+dfs(ind+1,0), dfs(ind+1,1))
            else:
                profit = max(p[ind]+dfs(ind+2,1),dfs(ind+1,0))
            
            return profit
        
        return dfs(0,1)