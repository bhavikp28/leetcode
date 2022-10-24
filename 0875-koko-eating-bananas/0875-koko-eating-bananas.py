import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
          # Binary Search
        # l, r = 1, max(piles)
        # HIS INNOVATION! 
        n, maxp, sump = len(piles), max(piles), sum(piles)
        if n == h: return maxp
        l, r = min(maxp, (sump-1)//h+1), min(maxp, (sump-1)//(h-n)+1)
        # l, r = (sump-1)//h+1, maxp
        if len(piles) == h: return r

        def time_taken(k):
            return sum(math.ceil(p/k) for p in piles)
        while l < r: 
            # print(f"l,r: {l,r}")
            mid = (l+r)//2
            time_mid = time_taken(mid)
            if time_mid > h: l = mid + 1
            elif time_mid <= h: r = mid            
        return r