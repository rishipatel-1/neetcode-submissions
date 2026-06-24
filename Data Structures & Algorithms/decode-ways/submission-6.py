class Solution:

    def numDecodings(self, s: str) -> int:

        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]

            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            one_digit = dfs(i + 1)

            two_digit = 0

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:

                two_digit = dfs(i + 2)

            memo[i] = one_digit + two_digit

            return memo[i]

        return dfs(0)