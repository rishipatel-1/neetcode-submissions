class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()

        res = []

        def backtrack(cur, start, target):

            if target == 0:
                res.append(cur.copy())
                return

            if target < 0:
                return

            prev = -1

            for i in range(start, len(candidates)):

                if candidates[i] == prev:
                    continue

                cur.append(candidates[i])

                backtrack(
                    cur,
                    i + 1,
                    target - candidates[i]
                )

                cur.pop()

                prev = candidates[i]

        backtrack([], 0, target)

        return res