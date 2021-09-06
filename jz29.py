# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        i, j, n, m = 0, 0, len(matrix), len(matrix[0])
        dir = "r"
        flag = [[True] * m for _ in range(n)]
        result = []
        while True:
            if dir == "r":
                if j < m and flag[i][j]:
                    result.append(matrix[i][j])
                    flag[i][j] = False
                    j += 1
                else:
                    dir = "d"
                    j -= 1
                    i += 1
                    if i < 0 or i >= n or j < 0 or j >= m or not flag[i][j]:
                        break
            elif dir == "d":
                if i < n and flag[i][j]:
                    result.append(matrix[i][j])
                    flag[i][j] = False
                    i += 1
                else:
                    dir = "l"
                    i -= 1
                    j -= 1
                    if i < 0 or i >= n or j < 0 or j >= m or not flag[i][j]:
                        break
            elif dir == "l":
                if j >= 0 and flag[i][j]:
                    result.append(matrix[i][j])
                    flag[i][j] = False
                    j -= 1
                else:
                    dir = "u"
                    j += 1
                    i -= 1
                    if i < 0 or i >= n or j < 0 or j >= m or not flag[i][j]:
                        break
            else:
                if i >= 0 and flag[i][j]:
                    result.append(matrix[i][j])
                    flag[i][j] = False
                    i -= 1
                else:
                    dir = "r"
                    i += 1
                    j += 1
                    if i < 0 or i >= n or j < 0 or j >= m or not flag[i][j]:
                        break
        return result
