#https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
            n = len(matrix)
            if n == 0:
                return False
            m = len(matrix[0])
            if m == 0 or matrix[0][0] > target or matrix[-1][-1] < target:
                return False
            
            row, col = 0, m - 1
            while row < n and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    col -= 1
                else:
                    row += 1
            
            return False
