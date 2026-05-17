# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Try 1

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 0 or len(str2) == 0: return ""
        if str1 + str2 != str2 + str1: return ""

        gcd_length = math.gcd(len(str1), len(str2))

        return str1[:gcd_length]

# Try2 

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 0 or len(str2) == 0: return ""
        if str1 + str2 != str2 + str1: return ""

        a,b = len(str1),len(str2)
        while b > 0:
            a,b = b, a%b

        return str1[:a]

        