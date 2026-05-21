# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:

        if len(s) == 0: return s

        vowels = []
        for i in s:
            if i in "AEIOUaeiou":
                vowels.append(i)

        new_s = ""

        for i in s:
            if i not in "AEIOUaeiou":
                new_s += i
            else:
                new_s += vowels.pop(-1)
        
        return new_s