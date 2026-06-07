# You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
# base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
# Return true if the given array is good, otherwise return false.
# Note: A permutation of integers represents an arrangement of these numbers.

# Try 1

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)

        tracker = 1

        for i in range(len(nums)):
            if (i == len(nums)-2) and (tracker == sorted_nums[i]) and (sorted_nums[-1] == sorted_nums[-2]):
                return True 
            elif sorted_nums[i] == tracker:
                tracker += 1
                continue
            return False
        return False
    
# try 2


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1

        if n <= 0:
            return False

        ideal_array = list(range(1, n)) + [n, n]

        return sorted(nums) == ideal_array