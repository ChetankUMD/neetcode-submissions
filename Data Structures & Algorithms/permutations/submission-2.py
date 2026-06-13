class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visit = [0]*len(nums)

        def dfs(path,visit):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if visit[i]==1:
                    continue
                path.append(nums[i])
                visit[i]=1
                dfs(path,visit)
                path.pop()
                visit[i]=0

        dfs([], visit)
        return res