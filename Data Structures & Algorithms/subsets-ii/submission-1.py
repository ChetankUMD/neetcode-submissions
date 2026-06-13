class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, path):
            if index == len(nums):
                res.append(path[:])
                return

            path.append(nums[index])
            dfs(index+1, path)
            path.pop()
            while index<len(nums)-1 and nums[index] == nums[index+1]:
                index+=1
            dfs(index+1, path)
    
        dfs(0,[])
        
        return res