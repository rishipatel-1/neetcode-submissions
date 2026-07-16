class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""

        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                stack.append([num, curr_str])
                curr_str =""
                num = 0 

            elif ch == "]":
                repeat , prev_str = stack.pop()
                curr_str = prev_str + curr_str * repeat

            else:
                curr_str += ch

        return curr_str        
            
        