class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1),len(word2)

        def dfs(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            ways = float("inf")
            if word1[i]==word2[j]:
                ways = dfs(i-1,j-1)
            else:
                ways = min(ways,1+dfs(i-1,j),1+dfs(i,j-1),1+dfs(i-1,j-1))
            
            return ways
        
        return dfs(m-1,n-1)