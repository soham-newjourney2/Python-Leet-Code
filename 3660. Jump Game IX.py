# You are given an integer array nums.

# From any index i, you can jump to another index j under the following rules:

# Jump to index j where j > i is allowed only if nums[j] < nums[i].
# Jump to index j where j < i is allowed only if nums[j] > nums[i].
# For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

# Return an array ans where ans[i] is the maximum value reachable starting from index i.


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        ans = [0] * n

        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], nums[i])

        ans[n - 1] = max(nums)
        suf_min = float('inf')
        
        for i in range(n - 1, -1, -1):
            if pre_max[i] > suf_min:
                ans[i] = ans[i + 1] if i + 1 < n else pre_max[i]
            else:
                ans[i] = pre_max[i]
            suf_min = min(suf_min, nums[i])
            
        return ans