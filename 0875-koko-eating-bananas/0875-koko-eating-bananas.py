import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = max(piles)

        def guess(n):
            hour = 0
            for i in piles:
                hour += math.ceil(i / n)
            #print(hour,n)
            if hour > h:
                return 1
            elif hour <= h:
                return -1

        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                k = min(k,mid)
                right = mid - 1
        return k