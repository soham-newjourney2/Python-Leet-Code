# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        length = max(len(word1), len(word2))

        for i in range(length):
            if len(word1)>i:
                new_word += word1[i]
            if len(word2)>i:
                new_word += word2[i]
        return new_word