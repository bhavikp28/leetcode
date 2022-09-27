class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        total = 0
        for i in nums:
            total = i + total
            output.append(total)
        return(output)