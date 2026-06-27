class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)

        for i in range(1,len(intervals)):
            interval1 = intervals[i-1]
            interval2 = intervals[i]

            if interval2.start < interval1.end:
                return False

        return True        
