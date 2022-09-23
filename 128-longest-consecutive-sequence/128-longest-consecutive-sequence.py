class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0
        for i in setnums:
            if (i - 1) not in setnums:
                count = 0
                while (i + count) in setnums:
                    count += 1
                if count > longest:
                    longest = count
        return longest
