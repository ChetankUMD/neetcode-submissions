class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        res = 0
        if len(num)%2==0:
            res = num[len(num)//2] + num[(len(num)//2)-1]
            res = res/2
        else:
            res = num[len(num)//2]
        
        return res


