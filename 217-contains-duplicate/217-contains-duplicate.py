class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers = set(nums)
        if len(nums) == len(numbers):
            return False
        return True