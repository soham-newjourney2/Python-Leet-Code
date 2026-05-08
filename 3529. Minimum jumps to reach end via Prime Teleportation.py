# You are given an integer array nums of length n.

# You start at index 0, and your goal is to reach index n - 1.

# From any index i, you may perform one of the following operations:

# Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
# Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
# Return the minimum number of jumps required to reach index n - 1.




class Solution:
    def minJumps(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 1: return 0

        prime_map = {}
        for i, x in enumerate(nums):
            d, temp = 2, x
            while d * d <= temp:
                if temp % d == 0:
                    prime_map.setdefault(d, []).append(i)
                    while temp % d == 0: temp //= d
                d += 1
            if temp > 1: prime_map.setdefault(temp, []).append(i)

        max_n = max(nums)
        is_p = [0, 0] + [1] * (max_n - 1)
        for p in range(2, int(max_n**0.5) + 1):
            if is_p[p]:
                for i in range(p*p, max_n + 1, p): is_p[i] = 0
        q, seen, seen_p = [(0, 0)], {0}, set()
        for i, d in q:
            if i == n - 1: return d
            
        
            moves = [i-1, i+1]
            v = nums[i]
            if v <= max_n and is_p[v] and v not in seen_p:
                moves += prime_map.get(v, [])
                seen_p.add(v)
                
            for nxt in moves:
                if 0 <= nxt < n and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))
        return -1

