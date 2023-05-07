class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for i,targ in enumerate(nums):
            if targ == target:
                ans.append(i)
        return ans