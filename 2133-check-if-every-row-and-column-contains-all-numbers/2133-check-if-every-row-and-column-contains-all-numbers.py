class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            used = set()
            for j in range(len(matrix)):
                elm = matrix[i][j]
                if elm >= 1 and elm <= len(matrix) and elm not in used:
                    used.add(elm)
                else:
                    return False
        for i in range(len(matrix)):
            used = set()
            for j in range(len(matrix)):
                elm = matrix[j][i]
                if elm >= 1 and elm <= len(matrix) and elm not in used:
                    used.add(elm)
                else:
                    return False
        return True