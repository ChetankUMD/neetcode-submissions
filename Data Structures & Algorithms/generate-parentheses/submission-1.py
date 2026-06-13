class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        open, close = 0,0
        st = []
        def dfs(open,close):
            if open==n and close == n:
                res.append("".join(st)) 
                return
            if open < n:
                st.append("(")
                dfs(open+1, close)
                st.pop()
            if close<open:
                st.append(")")
                dfs(open,close+1)
                st.pop() 

        dfs(0,0)
        return res              