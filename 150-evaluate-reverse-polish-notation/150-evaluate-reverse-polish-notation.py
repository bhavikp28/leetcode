class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        total = 0
        for i in tokens:
            if i == '+':
                total = nums[-1] + nums[-2]
                nums.pop()
                nums.pop()
                nums.append(int(total))
            elif i == '*':
                total = nums[-1] * nums[-2]
                nums.pop()
                nums.pop()
                nums.append(int(total))
            elif i == '/':
                total = nums[-2] / nums[-1]
                nums.pop()
                nums.pop()
                nums.append(int(total))
            elif i == '-':
                total = nums[-2] - nums[-1]
                nums.pop()
                nums.pop()
                nums.append(int(total))
            else:
                nums.append(int(i))
        total = int(total)
        return(nums[-1])