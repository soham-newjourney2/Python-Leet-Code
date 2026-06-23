# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i -k]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum/k