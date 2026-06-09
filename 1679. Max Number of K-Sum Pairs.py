# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_sort = sorted(nums)
        
        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if nums_sort[left] + nums_sort[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums_sort[left] + nums_sort[right] < k:
                left += 1
            else:
                right -= 1
        
        return count
