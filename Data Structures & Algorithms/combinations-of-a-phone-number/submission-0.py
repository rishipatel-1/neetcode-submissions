class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        phone = {

            "2": "abc",

            "3": "def",

            "4": "ghi",

            "5": "jkl",

            "6": "mno",

            "7": "pqrs",

            "8": "tuv",

            "9": "wxyz"

        }


        res = []

        path = []


        def dfs(i):

            if i == len(digits):

                res.append("".join(path))

                return


            digit = digits[i]


            # Choices

            for ch in phone[digit]:


                # Choose

                path.append(ch)


                # Go Deeper

                dfs(i + 1)


                # Undo

                path.pop()


        dfs(0)

        return res