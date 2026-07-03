class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):

            # Step 1: Take the last bit
            last_bit = n & 1

            # Step 2: Make space for the new bit
            res = res << 1

            # Step 3: Put the bit into the empty space
            res = res | last_bit

            # Step 4: Remove the bit we just used
            n = n >> 1

        return res