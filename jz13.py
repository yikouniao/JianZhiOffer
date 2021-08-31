# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        flag = [[False] * n for _ in range(m)]
        return self.dfs(0, 0, m, n, flag, k)

    def dfs(self, i, j, m, n, flag, k):
        if i == m or j == n or flag[i][j] or self.digit_sum(i) + self.digit_sum(j) > k:
            return 0
        flag[i][j] = True
        return 1 + self.dfs(i + 1, j, m, n, flag, k) + self.dfs(i, j + 1, m, n, flag, k)
    
    def digit_sum(self, i):
        return i % 10 + i // 10
