class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in matrix:
            hmap = {}
            for j in i:
                if j >= 1 and j <= len(matrix) and j not in hmap:
                    hmap[j] = 1
                else:
                    return False
        for i in range(len(matrix)):
            hmap = {}
            for j in range(len(matrix)):
                if matrix[j][i] >= 1 and matrix[j][i] <= len(matrix) and matrix[j][i] not in hmap:
                    hmap[matrix[j][i]] = 1
                else:
                    return False
        return True