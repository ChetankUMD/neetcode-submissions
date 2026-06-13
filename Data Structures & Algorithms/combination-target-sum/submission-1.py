class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, add, path):
            if add == target:
                res.append(list(path))
                return
            if add > target or index >= len(nums):
                return
            

            path.append(nums[index])
            dfs(index, add+nums[index], path)
            path.pop()
            dfs(index+1, add, path)

        dfs(0,0,[])

        return res