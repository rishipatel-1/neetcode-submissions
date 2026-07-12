class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count = {}

        for ch in t:
            count[ch] = count.get(ch,0) + 1

        l = 0    
        have = 0
        need = len(count)

        window = {}

        result = [-1,-1]

        result_length = float("inf")

        for r in range(len(s)):
            c = s[r]

            window[c] = window.get(c,0) + 1

            if c in count and window[c] == count[c]:
                have += 1

            while have == need:
                if (r-l+1) < result_length:
                    result = [l,r]
                    result_length = r-l+1
                window[s[l]] -= 1

                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1

        l , r = result

        return s[l:r+1] if result_length != float("inf") else ""            

                    






        




















        
            
            
                

            
        