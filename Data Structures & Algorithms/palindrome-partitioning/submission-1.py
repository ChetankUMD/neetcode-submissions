class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def palindrome(word):
            if len(word) == 1:
                return True
            l = 0
            r = len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True

        res = []
        st = []
        def dfs(i):
            if i>=len(s):
                res.append(st[:])
                return
            for j in range(i,len(s)):
                if palindrome(s[i:j+1]):
                    st.append(s[i:j+1])
                    dfs(j+1)
                    st.pop()
        

        
        dfs(0)
        return res
            
                