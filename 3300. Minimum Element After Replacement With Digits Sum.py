# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.

class Solution:
    def minElement(self, nums: List[int]) -> int:
        leastNum = float('inf')
        for num in nums:
            temp = 0
            while num > 0:
                temp += num % 10
                num //= 10
            if leastNum > temp:
                leastNum = temp
        return leastNum
        