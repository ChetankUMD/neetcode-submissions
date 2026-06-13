class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, total, path):
            if total == target:
                res.append(path.copy())
                return
            if index >= len(nums) or total > target:
                return
            print(path)
            path.append(nums[index])
            
            dfs(index+1,total+nums[index],path)
            path.pop()
            # print(path)
            while index<len(nums)-1 and nums[index] == nums[index+1]:
                index+=1
            dfs(index+1,total,path)

        dfs(0,0,[])
        return res