class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        dp = [[-1]*n2 for _ in range(n1)]
        def dfs(in1, in2):
            if in1 <0 or in2 <0:
                return 0
            if dp[in1][in2]!=-1:
                return dp[in1][in2]
            if s1[in1]==s2[in2]:
                dp[in1][in2]=1+dfs(in1-1,in2-1)
            else:
                dp[in1][in2]= max(dfs(in1-1,in2),dfs(in1,in2-1))
            return dp[in1][in2]
        
        return dfs(n1-1,n2-1)