class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        st = []
        res = 0

        for i in range(len(h)):
            start = i
            while st and st[-1][1] > h[i]:
                index, height = st.pop()
                area = height * (i - index)
                res = max(area, res)
                start = index
            st.append([start, h[i]])
        
        for i,hi in st:
            res = max(res, hi * (len(h) - i) )
        
        return res