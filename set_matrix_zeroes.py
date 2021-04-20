from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        temp = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    temp.append([r, c])

        for r, c in temp:
            for rr in range(len(matrix)):
                matrix[rr][c] = 0
            for cc in range(len(matrix[0])):
                matrix[r][cc] = 0

        return matrix
