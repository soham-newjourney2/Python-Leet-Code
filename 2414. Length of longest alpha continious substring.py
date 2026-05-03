# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
# For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
# Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

# test 1
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        long = []
        rt = ''
        counter = 0
        for i in range(len(s)):
            if counter == 0:
                counter = ord(s[i])
                rt = rt + s[i]
            else:
                if counter + 1 == ord(s[i]):
                    counter = ord(s[i])
                    rt = rt + s[i]
                else:
                    long.append(rt)
                    counter = ord(s[i])
                    rt = s[i]
        long.append(rt)
        return len(max(long, key=len))
    
# test 2
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if not s: return 0

        max_len = 1
        start = 0

        for i in range(1,len(s)):
            if ord(s[i]) != ord(s[i-1]) + 1:
                start = i
            cur_len = i - start + 1

            if cur_len > max_len:
                max_len = cur_len
        return max_len