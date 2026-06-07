# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        pre = 1
        for i in range(length):
            result[i] = pre
            pre *= nums[i]

        sub = 1
        for i in range(length - 1, -1, -1):
            result[i] *= sub
            sub *= nums[i]


        return result