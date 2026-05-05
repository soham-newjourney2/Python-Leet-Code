# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        list_of_word = s.split(" ")
        return len(list_of_word[-1])