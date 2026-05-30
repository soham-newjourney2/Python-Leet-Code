# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        while y != 0:
            answer = x ^ y
            carry = (x & y) << 1

            x = answer
            y = carry
        return bin(x)[2:]