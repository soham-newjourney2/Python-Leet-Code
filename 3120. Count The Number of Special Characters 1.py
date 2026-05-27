# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        result = [i.upper() for i in s if i.islower() and i.upper() in s]
        return len(result)