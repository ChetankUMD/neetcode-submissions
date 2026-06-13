class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        if n != len(s1)+len(s2):
            return False
        if n==0:
            return True

        def dfs(i1,i2,i3):
            if i3<0:
                return i1<0 and i2<0
            b = False
            if i2>=0 and s3[i3]==s2[i2]:
                b|= dfs(i1,i2-1,i3-1)
            if i1>=0 and s3[i3]==s1[i1]:
                print(s3)
                b|= dfs(i1-1,i2,i3-1)

            return b
        return dfs(len(s1)-1,len(s2)-1,n-1)