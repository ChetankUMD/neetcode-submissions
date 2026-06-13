class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(i, dots, curIp):
            if i==len(s) and dots==4:
                res.append(curIp[:-1])
                return
            
            if dots >4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if s[i]=="0" and i!=j:
                    continue
                if int(s[i:j+1]) <256:
                    dfs(j+1, dots+1, curIp+s[i:j+1]+".")
            
        dfs(0,0,"")
        return res
            