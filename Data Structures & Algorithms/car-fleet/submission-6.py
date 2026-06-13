class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        h = {}
        st = []
        for i in range(len(position)):
            h[position[i]] = speed[i]

        h = dict(sorted(h.items(), reverse=True))

        for k,v in h.items():
            time = (target - k)/v
            print(time)
            if st and time <= st[-1]:
                continue
            else:
                st.append(time)

        return len(st) 
