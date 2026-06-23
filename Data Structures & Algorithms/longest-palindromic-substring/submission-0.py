class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        answer = ""

        for i in range(n):
            dp[i][i] = True
            answer = s[i]


        for length in range(2,n+1):
            for l in range(n-length + 1):
                r = l + length - 1

                if s[l] == s[r]:

                    if length == 2:
                        dp[l][r] = True

                    elif dp[l+1][r-1]:
                        dp[l][r] = True 

                if dp[l][r]:
                    if length > len(answer):
                        answer = s[l:r+1]

        return answer                         
                        

 

            
        
            
        