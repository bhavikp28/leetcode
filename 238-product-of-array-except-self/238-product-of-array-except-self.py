class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums)+1)
        postfix = [1] * (len(nums)+1)
        ans = [1] * (len(nums))
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
            postfix[-2-i] = postfix[-1-i] * nums[-1-i]

        for i in range(len(nums)): 
            ans[i] = prefix[i] * postfix[i+1]
        return ans