class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = sorted(nums)
        arr = []
        for i in nums:
            arr.append(nums1.index(i))
        return(arr)