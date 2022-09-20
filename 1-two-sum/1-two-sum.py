class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = {}
        for i in range(len(nums)):
            if target - nums[i] in matches:
                return [matches[target - nums[i]],i]
            else:
                matches[nums[i]]=i
    