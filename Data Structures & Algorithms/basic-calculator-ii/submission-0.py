class Solution:
    def calculate(self, s: str) -> int:

        stack = []

        num = 0

        prevOp = "+"

        for i, ch in enumerate(s):

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in "+-*/" or i == len(s)-1:

                if prevOp == "+":
                    stack.append(num)

                elif prevOp == "-":
                    stack.append(-num)

                elif prevOp == "*":
                    stack.append(stack.pop() * num)

                else:
                    stack.append(int(stack.pop() / num))

                prevOp = ch
                num = 0

        return sum(stack)