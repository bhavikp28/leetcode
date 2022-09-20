class Solution:
    def calPoints(self, operations: List[str]) -> int:
        munch = []
        
        for i in range(len(operations)):
            if operations[i] == "C":
                munch.pop()
            elif operations[i] == "D":
                munch.append(munch[-1]*2)
            elif operations[i] == "+":
                munch.append(munch[-1]+munch[-2])
            else:
                munch.append(int(operations[i]))
                
        return (sum(munch))