class Solution:
    def maxProfit(self, p: List[int]) -> int:
        n = len(p)
        dp = [[-1]*2 for _ in range(n)]

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    buying = -p[ind]+dp[ind+1][0] if ind+1 <n else -p[ind]
                    notBuying = dp[ind+1][1] if ind+1 <n else 0
                    dp[ind][1] = max(buying, notBuying)
                else:
                    selling = p[ind]+dp[ind+2][1] if ind+2<n else p[ind]
                    notSelling = dp[ind+1][0] if ind+1 <n else 0
                    dp[ind][0] = max(selling,notSelling)
        return dp[0][1]

        # def dfs(ind, buy):
        #     if ind>=n:
        #         return 0
        #     if dp[ind][buy]!=-1:
        #         return dp[ind][buy]
        #     if buy:
        #         dp[ind][buy] = max(-p[ind]+dfs(ind+1,0), dfs(ind+1,1))
        #     else:
        #         dp[ind][buy] = max(p[ind]+dfs(ind+2,1),dfs(ind+1,0))
            
        #     return dp[ind][buy]
        
        # return dfs(0,1)