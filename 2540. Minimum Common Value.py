# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

# Try 1

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        def binarySearch(list1, target):
            low = 0
            high = len(list1) - 1

            while low <= high:
                mid = (low + high)//2

                if list1[mid] == target:
                    return 0
                elif list1[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        if len(nums1) == 0 or len(nums2) == 0: return -1

        ref_l = nums1 if len(nums1) <= len(nums2) else nums2
        ref_l2 = nums2 if len(nums1) <= len(nums2) else nums1

        for i in ref_l:
            if binarySearch(ref_l2, i) == 0:
                return i
        return -1


# Try 2

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i,j = 0,0
        len1,len2 = len(nums1),len(nums2)

        while i<len1 and j<len2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
    
