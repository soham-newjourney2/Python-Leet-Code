# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

# test 1
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = s[1:len(s)] + s[0]
            if s == goal:
                return True
        return False
    
# test 2
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)
        if l != len(goal):
            return False
        if l == 0:
            return True

        for i in range(l):
            match = True
            for j in range(l):
                if (s[j] != goal[(i+j)%l]):
                    match = False
            if match:
                return True

        return False
    