class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r,l2 = 0,0,0

        while l == 0 or l != r:
            print(1)
            l = nums[l]
            r = nums[nums[r]]

        while l != l2:
            l = nums[l]
            l2 = nums[l2]
        return l