# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_L = sorted(nums1 + nums2)
        l = len(new_L)

        mid = l // 2
        
        if l % 2 == 0:
            return (new_L[mid - 1] + new_L[mid]) / 2.0
        else:
            return float(new_L[mid])