# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
# Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counter = 0
        last_lower = {}
        first_upper = {}

        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            elif char.isupper():
                if char not in first_upper:
                    first_upper[char] = i

        
        for i in last_lower:
            if i.upper() in first_upper and last_lower[i] < first_upper[i.upper()]:
                counter += 1

       
        return counter


