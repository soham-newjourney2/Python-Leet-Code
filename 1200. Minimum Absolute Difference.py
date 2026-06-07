# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < 
# b - a equals to the minimum absolute difference of any two elements in arr


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)

        min_num = float('inf')
        sub = []

        for i in range(len(arr)-1):
            if sorted_arr[i+1] - sorted_arr[i] < min_num:
                min_num = sorted_arr[i+1] - sorted_arr[i]
                sub.clear()
                sub.append([sorted_arr[i], sorted_arr[i+1]])
            elif sorted_arr[i+1] - sorted_arr[i] > min_num:
                continue
            else:
                sub.append([sorted_arr[i], sorted_arr[i+1]])

        return sub 

        