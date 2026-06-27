class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for interval in intervals:

            # Case 1: Current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)

            # Case 2: Current interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[intervals.index(interval):]

            # Case 3: Overlap → Merge
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

        res.append(newInterval)

        return res