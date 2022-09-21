import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for key, value in freq.items():
            if len(ans) < k:
                heapq.heappush(ans, [value,key])
            else:
                heapq.heappushpop(ans, [value,key])
        return [key for value, key in ans]