class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]

            if i == len(s):
                return True

            for j in range(i, len(s)):

                word = s[i:j+1]

                if word in wordDict and dfs(j + 1):

                    memo[i] = True

                    return True

            memo[i] = False

            return False

        return dfs(0)