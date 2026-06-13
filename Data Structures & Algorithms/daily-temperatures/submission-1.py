class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        st = []
        res = [0] * len(t)
        for i in range(len(t)):
            while st and t[st[-1]] < t[i]:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)

        return res