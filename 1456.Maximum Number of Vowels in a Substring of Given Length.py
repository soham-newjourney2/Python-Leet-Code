# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(1 for i in range(k) if s[i] in vowels)
        maxx = count

        for i in range(k,len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            if count > maxx:
                maxx = count
            if count == k:
                return count
        return maxx
        