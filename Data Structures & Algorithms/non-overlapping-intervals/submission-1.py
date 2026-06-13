class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        output = []
        output.append(intervals[0])
        n=len(intervals)
        i =0
        res = 0

        for start, end in intervals:
            lastend = output[-1][1]
            if start < lastend:
                continue
            else:
                output.append([start,end])
        return len(intervals)-len(output)
        # while i<n-1:
        #     if intervals[i][1] > intervals[i+1][0]:
        #         res+=1
        #     i+=1
        
        # return res