class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []

        def dfs(i, st):
            if len(st)==len(digits):
                res.append(st[:])
                return
            for c in h[digits[i]]:
                dfs(i+1,st+c)
        
        if digits:
            dfs(0,"")

        return res
            
