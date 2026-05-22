# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if max(letters) <= target: return letters[0]
        small = 'z'

        for i in letters:
            if i > target and i < small:
                small = i

        return small
        