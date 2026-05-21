# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1: return s
        s = s.strip()
        new_l = s.split()
        new_s = ""

        for i in range(1, len(new_l) + 1):
            new_s += new_l[i * -1].strip() + " "

        return new_s.strip()


        