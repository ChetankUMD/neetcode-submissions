class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        # length = 1
        for i in range(n):
            dp[i][i] = True

        # length = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        res = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]==True:
                    res+=1
        return res