class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[List[int]]) -> List[List[int]]:

        res = []

        for interval in intervals:

            # Current interval is completely before new interval
            if interval[1] < newInterval[0]:
                res.append(interval)

            # New interval comes before everything else
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[intervals.index(interval):]

            # Overlap → keep expanding the new interval
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

        # Add the merged/new interval at the end
        res.append(newInterval)

        return res